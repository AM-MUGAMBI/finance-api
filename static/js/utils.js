// Redirect to login if user is not authenticated
function requireAuth() {
    const token = localStorage.getItem("token");
    if (!token) {
        window.location.href = "/"; // login page
    }
}

// Get stored token
function getToken() {
    return localStorage.getItem("token");
}

// Logout
function logout() {
    localStorage.removeItem("token");
    window.location.href = "/"; // login page
}

// Fetch wrapper with auth
async function apiGet(url) {
    const res = await fetch(url, {
        headers: { "Authorization": `Bearer ${getToken()}` }
    });
    return await res.json();
}
