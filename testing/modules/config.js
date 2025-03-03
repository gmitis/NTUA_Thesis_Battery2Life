// fields from python ORM models that values need be unique
const inputFile = __ENV.FILE_PATH;
export const input = JSON.parse(open(inputFile));
export const inputValidity = inputFile.includes("invalid") ? false : true;

export const BASE_URL = "https://dev-battery2life.iccs.gr";

// list of endpoints with their allowed methods
export const endpoints = {
    "/api/batteries/": ["GET", "POST"],
    "/api/batteries/{id}/": ["GET", "PUT", "PATCH", "DELETE"],

    "/api/modules/": ["GET", "POST"],
    "/api/modules/{id}/": ["GET", "PUT", "PATCH", "DELETE"],

    "/api/cells/": ["GET", "POST"],
    "/api/cells/{id}/": ["GET", "PUT", "PATCH", "DELETE"],
    
    "/api/measurements/": ["GET", "POST"],
    "/api/measurements/{id}/": ["GET", "PUT", "PATCH", "DELETE"],
    
    "/api/eis/": ["GET", "POST"],
    "/api/eis/{id}/": ["GET", "PUT", "PATCH", "DELETE"],
    
    "/api/chemical/": ["GET", "POST"],
    "/api/chemical/{id}/": ["GET", "PUT", "PATCH", "DELETE"],

    "/api/manufacturers/": ["GET", "POST"],
    "/api/manufacturers/{id}/": ["GET", "PUT", "PATCH", "DELETE"],

    "/api/material/": ["GET", "POST"],
    "/api/material/{id}/": ["GET", "PUT", "PATCH", "DELETE"],

    "/api/safety_feature/": ["GET", "POST"],
    "/api/safety_feature/{id}/": ["GET", "PUT", "PATCH", "DELETE"],
};
