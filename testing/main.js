// TODO:
//      - split code into functions in test.js
//      - create function that gets length and creates valid + invalid input.json, change performTest to have the necessary length required when called from main

import http from "k6/http";
import { check } from "k6";
import { performTest } from "./modules/test.js";
import { updateClassificationMetrics } from "./modules/metrics.js";
import { BASE_URL, input, inputValidity, endpoints } from "./modules/config.js";


// k6 configuration options
// Add thresholds for your metrics to ensure they appear in the summary
export const options = {
    scenarios: {
        normal_load_test: {
            executor: 'ramping-arrival-rate',
            startRate: 1,
            timeUnit: '1s',
            preAllocatedVUs: 5,
            maxVus: 5,
            stages: [
                { target: 1, duration: '1m'},
                { target: 2, duration: '2m'},
                { target: 5, duration: '1m'},
                { target: 0, duration: '1m'},
            ]
        },
        heavy_load_test: {
            executor: 'ramping-vus',
            startVUs: 0,
            stages: [
                { duration: '1m', target: 25 },  
                { duration: '2.5m', target: 25 }, 
            ],
            gracefulRampDown: '30s',
        },
    },
    summaryTrendStats: ["min", "med", "max", "avg", "p(90)", "p(95)", "p(99)"],    
    thresholds: {
        FN: ["count>=0"],  
        FP: ["count>=0"],  
        TN: ["count>=0"],  
        TP: ["count>=0"],  
        accuracy: ["rate>=0"],
        misclassification: ["rate>=0"],
        precision: ["rate>=0"],
        sensitivity: ["rate>=0"],
        specificity: ["rate>=0"]
    }
};


// get JWT token by authentication (applicable to all of the requests)
export function setup() {
    // get JWT token
    const params = { headers: { "Content-Type": "application/json" } };
    const payload = JSON.stringify({
        username: "admin",
        password: "admin",
    });
    const res = http.post(`${BASE_URL}/api/token/`, payload, params);

    // Error handling for failed authentication
    check(res, {
        "check if status 200": (r) => r.status === 200,
    });
    if (res.status !== 200) {
        console.error("Authentication failed:", res.status, res.body);
        return null;
    }

    try {
        const token = res.json("access");
        return token;
    } catch (e) {
        console.error("Failed to parse token from response:", e);
        return null;
    }
}


export default function (data) {
    // setup authentication
    if (!data) {
        console.error("No authentication token available");
        return;
    }

    const params = {
        headers: {
            Authorization: `Bearer ${data}`,
            "Content-Type": "application/json",
        },
    };

    // perform request for every endpoint
    for (let endpoint in endpoints) {
        let inp = input[endpoint];
        
        performTest(endpoint, params, inp, inputValidity);
    }

    // produce accuracy, precision, missclassification, sensitivity, specificity metrics
    updateClassificationMetrics();    
}
