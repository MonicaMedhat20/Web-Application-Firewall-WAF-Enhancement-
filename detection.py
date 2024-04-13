from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib import request, parse, error
import pandas as pd
import sys
from pycaret.classification import load_model, predict_model
from tenacity import retry
from poetry import pycaret 

badwords = ['sleep', 'drop', 'uid', 'select', 'waitfor', 'delay', 'system', 'union', 'order by', 'group by', 'where', 'from']

def ExtractFeatures(path):
    path = parse.unquote(path)
    badwords_count = 0
    single_q = path.count("*")
    double_q = path.count("\"")
    dashes = path.count(" -- ")
    braces = path.count("(")
    spaces = path.count(" ")
    for word in badwords:
        badwords_count += path.count(word)
    lst = [single_q, double_q, dashes, braces, spaces, badwords_count]
    print(lst)
    return pd.DataFrame([lst], columns=['single_q', 'double_q', 'dashes', 'braces', 'spaces', 'badwords'])

# Load the Random Forest model using pycaret
model = load_model('model.pkl')
model2 = load_model('model2.pkl')

class SimpleHTTPProxy(SimpleHTTPRequestHandler):
    proxy_routes = {}

    @classmethod
    def set_routes(cls, proxy_routes):
        cls.proxy_routes = proxy_routes
    
    def do_GET(self):
        parts = self.path.split('/')
        print(parts)
        live_data = ExtractFeatures(parts[3])
        result = predict_model(model, data=live_data)
        print(result)
        if result.iloc[0, 1] == 1:
            print('Intrusion Detected')
            if len(parts) >= 2:
                self.proxy_request('http://' + parts[2] + '/')
            else:
                super().do_GET()

    def proxy_request(self, url):
        try:
            response = request.urlopen(url)
        except error.HTTPError as e:
            print('Error:', e)
            self.send_response_only(e.code)
            self.end_headers()
            return
        self.send_response_only(response.status)
        for name, value in response.headers.items():
            self.send_header(name, value)
        self.end_headers()
        self.copyfile(response, self.wfile)

SimpleHTTPProxy.set_routes({'proxy_route': 'http://127.0.0.1:5000/'})
with HTTPServer(('127.0.0.1', 5000), SimpleHTTPProxy) as httpd:
    host, port = httpd.socket.getsockname()
    print(f'Listening on http://{host}:{port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)
