import http from 'k6/http';
import { check } from 'k6';
import { updateMetrics } from "./metrics.js";
import { areObjectsEqual } from './helpers.js';
import { BASE_URL, endpoints } from "./config.js";


// input (endpoint uri, array http.methods)
// output(object metrics: { accuracy:float,  misclassification:float, precision:float, sensitivity:float, specificity:float })
export const performTest = (endpoint, params, input, inputValidity, inputLen) => {
    let methods = endpoints[endpoint];
    
    // for each method of the endpoint and each input of the method, check the output and update metrics
    if (endpoint.includes("{id}/")) {
        endpoint = endpoint.replace("{id}/", "");
        const ids = Array.from({ "length": inputLen }, () => Math.floor(Math.random() * 1000 + 1));
        const urls = ids.map((id) => `${BASE_URL}${endpoint}${id}`);

        // for each allowed method of the given endpoint
        // perform requests for 5 inputs, validate output, update metrics
        for (let method of methods) {

            if (method === "GET") {
 
                for (let url of urls) {
                    let res = http.get(url, params);
                    let isValid = check(res, {
                        "(GET/id): Status is 200": (r) => r.status === 200,
                        "(GET/id): We get an item as a response": (r) => {
                            let len = r.status === 200 ? r.json().length : 0;
                            return len === 1;
                        },
                    });
                    updateMetrics(isValid, inputValidity);
                }

            } else if (method === "PUT") {

                let i = 0;
                for (let body of input["PUT"]) {
                    const res = http.put(urls[i], body, params);
                    const isValid = check(res, {
                        "(PUT/id): Status is 200": (r) => r.status === 200 || r.status === 204,
                        "(PUT/id): We get an item as a response": (r) => {
                            let len = r.status === 200 ? r.json().length : 0;
                            return len === 1;
                        },
                    });
                    updateMetrics(isValid, inputValidity);
                    i++;
                }

            } else if (method === "PATCH")  {

                let i = 0;
                for (let body of input["PATCH"]) {
                    const res = http.patch(urls[i], body, params);
                    const isValid = check(res, {
                        "(PATCH/id): Status is 200": (r) => r.status === 200 || r.status === 204,
                        "(PATCH/id): We get an item as a response": (r) => {
                            let len = r.status === 200 ? r.json().length : 0;
                            return len === 1;
                        },
                    });
                    updateMetrics(isValid, inputValidity);
                    i++;
                }

            } else if (method === "DELETE") {

                for (let url of urls) {
                    let res = http.del(url, params);
                    let isValid = check(res, { "(DELETE/id): Status is 204": (r) => r.status === 204 });
                    updateMetrics(isValid, inputValidity);
                }
            }
        }

    } else {
        for (let method of methods) {

            let url = `${BASE_URL}${endpoint}`;

            if (method === "GET") {

                let res = http.get(url, params);
                let isValid = check(res, {
                    "(GET): Status is 200": (r) => r.status === 200,
                    "(GET): Response is JSON": (r) => r.headers["Content-Type"].includes("application/json"),
                    "(GET): We get items as a response": (r) => {
                        let len = r.status === 200 ? r.json().length : 0;
                        return len === 1000;
                    },
                });

                updateMetrics(isValid, inputValidity);

            } else if (method === "POST") {

                for (let body of input["POST"]) {
                    let res = http.post(url, body, params);
                    let resData = res.json();
                    let isValid = check(res, {
                        "(POST): Status is 201": (r) =>  r.status === 201,
                        "(POST): Response is JSON": (r) =>  r.headers["Content-Type"].includes("application/json"),
                        "(POST): Correct object written": (r) =>  areObjectsEqual(body, resData)
                    });

                    updateMetrics(isValid, inputValidity);
                }

            }

        }

    }
};
