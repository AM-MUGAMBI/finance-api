
const API_URL = "http://127.0.0.1:8000";

async function apiGet(endpoint) {
    return fetch(API_URL + endpoint, {
        headers: { "Authorization": "Bearer " + getToken() }
    }).then(r => r.json());
}

async function apiPost(endpoint, body) {
    return fetch(API_URL + endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + getToken()
        },
        body: JSON.stringify(body)
    }).then(r => r.json());
}
