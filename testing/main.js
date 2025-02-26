// TODO:
//      - split code into functions in test.js
//      - create function that gets length and creates valid + invalid input.json, change performTest to have the necessary length required when called from main

import http from "k6/http";
import { sleep, check } from "k6";
import { performTest } from "./modules/test.js";
import { BASE_URL, valid_input, invalid_input, endpoints } from "./modules/config.js";


// k6 configuration options
export const options = {
    //   stages: [{ duration: "10s", target: 30 }],
    vus: 1,
    iterations: 1,
    duration: "3s",
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
        let vi = valid_input[endpoint];
        let ivi = invalid_input[endpoint];

        performTest(endpoint, params, vi, true, 5);
        performTest(endpoint, params, ivi, false, 5);
    }

    sleep(1);
}
