from flask import Flask, request, abort

app = Flask(__name__)

# Simulated database to check for brute force attacks
users = {
    "admin": {"password": "securepassword", "login_attempts": 0}
}

# Basic WAF function
def waf(request):
    # SQL injection prevention
    for value in request.values.values():
        if any(keyword in value for keyword in ["SELECT", "INSERT", "UPDATE", "DELETE"]):
            abort(403)

    # Cross-Site Scripting (XSS) prevention
    for value in request.values.values():
        if "<script>" in value:
            abort(403)

    # Brute force protection
    if request.path == '/login' and request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users:
            if users[username]["login_attempts"] >= 3:
                abort(403)  # Block the request if there have been 3 or more login attempts

            if password != users[username]["password"]:
                users[username]["login_attempts"] += 1
                abort(403)  # Block the request for incorrect password

    # Allow normal requests
    return None

@app.route('/login', methods=['POST'])
def login():
    waf(request)
    # Your authentication logic here
    return 'Login successful'

@app.route('/')
def index():
    waf(request)
    return 'Hello, World!'
