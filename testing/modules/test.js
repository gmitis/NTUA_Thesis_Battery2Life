// TODO: 
//      - make testing for /api/measurements/ idempotent (DELETE all)
//      - revert automatic ids to pre testing levels

import http from 'k6/http';
import { check } from 'k6';
import { updateMetrics } from "./metrics.js";
import { getUniqueRandomNumber } from './helpers.js';
import { BASE_URL, endpoints } from "./config.js";

let postIds = [];
let urls = [];

// input (endpoint uri, array http.methods)
// output(object metrics: { accuracy:float,  misclassification:float, precision:float, sensitivity:float, specificity:float })
export const performTest = (endpoint, params, input, inputValidity, inputLen) => {
    let methods = endpoints[endpoint];
    
    // for each method of the endpoint and each input of the method, check the output and update metrics
    if (!endpoint.includes("{id}/")) {
        for (let method of methods) {

            let url = `${BASE_URL}${endpoint}`;

            if (method === "GET") {
                if (!inputValidity) continue;

                let res = http.get(url, params);
                let isValid = check(res, {
                    "(GET): Status is 200": (r) => r.status === 200,
                    "(GET): Response is JSON": (r) => r.headers["Content-Type"].includes("application/json"),
                    "(GET): We get items as a response": (r) => {
                        let len = r.status === 200 ? r.json().length : 0;
                        return len !== 0;
                    },
                });

                updateMetrics(isValid, inputValidity);

            } else if (method === "POST") {

                for (let body of input["POST"]) {
                    let res = http.post(url, JSON.stringify(body), params);
                    let id = res.json()["id"];
                    if (id) postIds.push(id)

                    let isValid = check(res, {
                        "(POST): Status is 201": (r) =>  r.status === 201 || r.status === 200,
                        "(POST): Response is JSON": (r) =>  r.headers["Content-Type"].includes("application/json"),
                        "(POST): Correct object written": (r) => {
                            let len = 0;
                            if (r.status === 201 || r.status === 200) {
                               len = Object.keys(r.json()).length;
                            }   
                            return len > 1;
                        }
                    });  
                    
                    
                    updateMetrics(isValid, inputValidity);
                }

            }

        }
    } else  {
        // generate urls with ids, to be used by the http.method requests
        endpoint = endpoint.replace("{id}/", "");
        if (endpoint.includes("measurements") && inputValidity) {
            urls =  [...Array(5)].map(() => `${BASE_URL}${endpoint}${getUniqueRandomNumber(1, 1000)}/`);
        } else if (!inputValidity){
            urls =  [...Array(5)].map(() => `${BASE_URL}${endpoint}${Math.floor(Math.random() * 1000) + 1}/`);
            urls.push(10923);
        } else {
            urls = postIds.map((id) => `${BASE_URL}${endpoint}${id}/`);
        }

        // for each allowed method of the given endpoint
        // perform requests for 5 inputs, validate output, update metrics
        for (let method of methods) {

            if (method === "GET") {
                if (!inputValidity){
                    urls =  [...Array(5)].map(() => `${BASE_URL}${endpoint}${Math.floor(Math.random() * 1000) + 1000000}/`);
                }
 
                for (let url of urls) {
                    let res = http.get(url, params);

                    let isValid = check(res, {
                        "(GET/id): Status is 200": (r) => r.status === 200,
                        "(GET/id): We get a valid item as a response": (r) => {
                            let res_id = r.json()["id"]; 
                            let id = url.replace(/.*\/(\d+)\/$/, "$1");
                            return res_id == id;
                        }
                    });
                    updateMetrics(isValid, inputValidity);
                }

                if (!inputValidity){
                    urls =  [...Array(5)].map(() => `${BASE_URL}${endpoint}${Math.floor(Math.random() * 1000) + 1}/`);
                }

            } else if (method === "PUT") {

                let i = 0;
                for (let body of input["PUT"]) {
                    const res = http.put(urls[i], JSON.stringify(body), params);
                    const isValid = check(res, {
                        "(PUT/id): Status is 200": (r) => r.status === 200 || r.status === 204,
                        "(PUT/id): We get an item as a response": (r) => {
                            let len = r.status === 200 ? Object.keys(r.json()).length : 0;
                            return len > 1;
                        }
                    });
                    updateMetrics(isValid, inputValidity);
                    i++;
                }

            } else if (method === "PATCH")  {

                let i = 0;
                for (let body of input["PATCH"]) {
                    const res = http.patch(urls[i], JSON.stringify(body), params);
                    const isValid = check(res, {
                        "(PATCH/id): Status is 200": (r) => r.status === 200 || r.status === 204,
                        "(PATCH/id): We get an item as a response": (r) => {
                            let len = r.status === 200 ? Object.keys(r.json()).length : 0;
                            return len > 0;
                        },
                    });
                    updateMetrics(isValid, inputValidity);
                    i++;
                }

            } else if (method === "DELETE") {
                if (!inputValidity){
                    urls =  [...Array(5)].map(() => `${BASE_URL}${endpoint}${Math.floor(Math.random() * 1000) + 1000000}/`);
                }

                for (let url of urls) {
                    let res = http.del(url, null, params);
                    let isValid = check(res, { "(DELETE/id): Status is 204": (r) => r.status === 204 });
                    updateMetrics(isValid, inputValidity);
                }

                urls = [];
                postIds = [];
            }
        }

    } 
};
