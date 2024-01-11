from flask import Flask, request, abort

app = Flask(__name__)

def positive_security_waf(request):
    # Positive Security Model: Allow only alphanumeric characters in parameters
    for value in request.values.values():
        if not value.isalnum():
            abort(403)

@app.route('/')
def index():
    positive_security_waf(request)
    return 'Hello, World!'

@app.route('/login', methods=['POST'])
def login():
    positive_security_waf(request)
    # Your authentication logic here
    return 'Login successful'

if __name__ == '__main__':
    app.run(debug=True)
