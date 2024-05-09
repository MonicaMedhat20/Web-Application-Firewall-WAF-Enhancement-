from flask import Flask, request, jsonify
import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder
import pickle
from urllib.parse import urlparse

# Lists of common SQL injection and XSS patterns
SQL_INJECTION_PATTERNS = [
    "select", "union", "insert", "update", "delete", "drop", "table", "information_schema",
    "--", ";", "/*", "*/", "@@", "char", "concat", "xp_", "sp_", "exec", "' OR '1'='1"
]

XSS_PATTERNS = [
    "<script", "javascript:", "onerror=", "onload=", "onmouseover=", "alert(", "document.cookie",
    "document.write", "eval(", "<iframe", "<img", "src="
]

def contains_security_risks(text):
    """Check if the input text contains any potential SQL injection or XSS patterns."""
    text_lower = text.lower()
    for pattern in SQL_INJECTION_PATTERNS:
        if pattern in text_lower:
            return 1
    for pattern in XSS_PATTERNS:
        if pattern in text_lower:
            return 1
    return 0

# Feature extraction from URL
def extract_features_from_url(url):
    """Extract HTTP request features from a given URL."""
    http_request = {
        'Method': 'GET',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-encoding': 'gzip, deflate, br',
        'Accept-charset': 'UTF-8',
        'language': 'en-US,en;q=0.5',
        'host': '',
        'cookie': 'JSESSIONID=ABCDE12345',
        'content-type': 'application/x-www-form-urlencoded',
        'connection': 'keep-alive',
        'length': 'Content-Length: 123',
        'content': 'param1=value1&param2=value2',
        'URL': url
    }

    url_parts = re.match(r"(http[s]?://)?([^/]+)(/.*)", url)
    if url_parts:
        http_request['host'] = url_parts.group(2)

    return pd.DataFrame([http_request])

# Preprocess and encode features
def preprocess_and_encode(url_df):
    """Preprocess and encode the features extracted from a given URL."""
    lb_make = LabelEncoder()

    def count_dot(url): return url.count('.')
    def no_of_dir(url): return urlparse(url).path.count('/')
    def no_of_embed(url): return urlparse(url).path.count('//')
    def shortening_service(url): return 1 if re.search(r'bit\.ly|goo\.gl', url) else 0
    def count_http(url): return url.count('http')
    def count_per(url): return url.count('%')
    def count_ques(url): return url.count('?')
    def count_hyphen(url): return url.count('-')
    def count_equal(url): return url.count('=')
    def url_length(url): return len(url)
    def hostname_length(url): return len(urlparse(url).netloc)
    def suspicious_words(url): return sum(word in url.lower() for word in ['error', 'select', 'password'])
    def digit_count(url): return sum(char.isdigit() for char in url)
    def letter_count(url): return sum(char.isalpha() for char in url)
    def count_special_characters(url): return len(re.sub(r'[a-zA-Z0-9\s]', '', url))

    url_df['count_dot_url'] = url_df['URL'].apply(count_dot)
    url_df['count_dir_url'] = url_df['URL'].apply(no_of_dir)
    url_df['count_embed_domain_url'] = url_df['URL'].apply(no_of_embed)
    url_df['short_url'] = url_df['URL'].apply(shortening_service)
    url_df['count-http'] = url_df['URL'].apply(count_http)
    url_df['count%_url'] = url_df['URL'].apply(count_per)
    url_df['count?_url'] = url_df['URL'].apply(count_ques)
    url_df['count-_url'] = url_df['URL'].apply(count_hyphen)
    url_df['count=_url'] = url_df['URL'].apply(count_equal)
    url_df['url_length'] = url_df['URL'].apply(url_length)
    url_df['hostname_length_url'] = url_df['URL'].apply(hostname_length)
    url_df['sus_url'] = url_df['URL'].apply(suspicious_words)
    url_df['count-digits_url'] = url_df['URL'].apply(digit_count)
    url_df['count-letters_url'] = url_df['URL'].apply(letter_count)
    url_df['special_count_url'] = url_df['URL'].apply(count_special_characters)

    url_df["Method_enc"] = lb_make.fit_transform(url_df["Method"])
    url_df["host_enc"] = lb_make.fit_transform(url_df["host"])

    labels = [
        'count_dot_url', 'count_dir_url', 'count_embed_domain_url', 'count-http',
        'count%_url', 'count?_url', 'count-_url', 'count=_url', 'url_length', 'hostname_length_url',
        'sus_url', 'count-digits_url', 'count-letters_url', 'Method_enc'
    ]

    return url_df[labels]

# Model prediction function with security risk check
def predict_from_url(url, model_path='model.pkl'):
    """Predict the classification for a given URL using a pre-trained model."""
    security_risk_check = contains_security_risks(url)
    if security_risk_check == 1:
        return 1

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    url_df = extract_features_from_url(url)
    processed_features = preprocess_and_encode(url_df)

    prediction = model.predict(processed_features)
    return prediction[0]

# URLChecker class
class URLChecker:
    def __init__(self, data_path='combined_balanced_urls.csv'):
        """Initialize the URL checker with a specific dataset path."""
        self.data_path = data_path
        self.data = pd.read_csv(self.data_path)

    def check_url(self, url: str) -> int:
        """Check the status of a given URL in the dataset.

        Args:
            url (str): The URL to check.

        Returns:
            int: 0 if the URL is found and benign, otherwise 1.
        """
        found = self.data[self.data['url'] == url]
        if not found.empty and found.iloc[0]['label'] == 'benign':
            return 0
        else:
            return 1

# Create Flask application
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """Flask endpoint to predict security risks based on a submitted URL."""
    data = request.json
    url = data.get('url', '')

    # Load the URL checker
    with open('url_checker.pkl', 'rb') as f:
        url_checker = pickle.load(f)

    # Predict security risks
    result = predict_from_url(url)

    if result == 1:
        # If the result is 1, check the URL with URLChecker
        url_check_result = url_checker.check_url(url)
        if url_check_result == 0:
            return jsonify({"result": "Benign"})
        else:
            return jsonify({"result": "Attack"})
    

if __name__ == "__main__":
    # Save the URLChecker instance
    checker = URLChecker('combined_balanced_urls.csv')  # Update with actual path
    with open('url_checker.pkl', 'wb') as f:
        pickle.dump(checker, f)

    app.run(port=9005)
