import re
from urllib.parse import urlparse
import pandas as pd
import pickle
# from ML(csicdataset) import suspicious_words


def suspicious_words(url):
    score_map = {
        'error': 30,
        'errorMsg': 30,
        'id': 10,
        'errorID': 30,
        'SELECT': 50,
        'FROM': 50,
        'WHERE': 50,
        'DELETE': 50,
        'USERS': 50,
        'DROP': 50,
        'CREATE': 50,
        'INJECTED': 50,
        'TABLE': 50,
        'alert': 30,
        'javascript': 20,
        'cookie': 25,
        '--': 30,
        '.exe': 30,
        '.php': 20,
        '.js': 10,
        'admin': 10,
        'administrator': 10,
        '\'': 30,
        'password': 15,
        'login': 15,
        'incorrect': 20,
        'pwd': 15,
        'tamper': 25,
        'vaciar': 20,
        'carrito': 25,
        'wait': 30,
        'delay': 35,
        'set': 20,
        'steal': 35,
        'hacker': 35,
        'proxy': 35,
        'location': 30,
        'document.cookie': 40,
        'document': 20,
        'set-cookie': 40,
        'create': 40,
        'cmd': 40,
        'dir': 30,
        'shell': 40,
        'reverse': 30,
        'bin': 20,
        'cookiesteal': 40,
        'LIKE': 30,
        'UNION': 35,
        'include': 30,
        'file': 20,
        'tmp': 25,
        'ssh': 40,
        'exec': 30,
        'cat': 25,
        'etc': 30,
        'fetch': 25,
        'eval': 30,
        'wait': 30,
        'malware': 45,
        'ransomware': 45,
        'phishing': 45,
        'exploit': 45,
        'virus': 45,
        'trojan': 45,
        'backdoor': 45,
        'spyware': 45,
        'rootkit': 45,
        'credential': 30,
        'inject': 30,
        'script': 25,
        'iframe': 25,
        'src=': 25,
        'onerror': 30,
        'prompt': 20,
        'confirm': 20,
        'eval': 25,
        'expression': 30,
        'function\(': 20,
        'xmlhttprequest': 30,
        'xhr': 20,
        'window.': 20,
        'document.': 20,
        'cookie': 25,
        'click': 15,
        'mouseover': 15,
        'onload': 20,
        'onunload': 20,
    }

    matches = re.findall(r'(?i)' + '|'.join(score_map.keys()), url)

    total_score = sum(score_map.get(match.lower(), 0) for match in matches)
    return total_score



def extract_features(url, content):
    features = {}
    
    # URL features
    features['count_dot_url'] = url.count('.')
    features['count_dir_url'] = urlparse(url).path.count('/')
    features['count_embed_domain_url'] = urlparse(url).path.count('//')
    features['count-http'] = url.count('http')
    features['count%_url'] = url.count('%')
    features['count?_url'] = url.count('?')
    features['count-_url'] = url.count('-')
    features['count=_url'] = url.count('=')
    features['url_length'] = len(url)
    features['hostname_length_url'] = len(urlparse(url).netloc)
    features['sus_url'] = suspicious_words(url)
    features['count-digits_url'] = sum(c.isdigit() for c in url)
    features['count-letters_url'] = sum(c.isalpha() for c in url)
    features['number_of_parameters_url'] = len(urlparse(url).query.split('&'))
    features['number_of_fragments_url'] = len(urlparse(url).fragment.split('#')) - 1
    features['is_encoded_url'] = int('%' in url.lower())
    features['special_count_url'] = len(re.sub(r'[a-zA-Z0-9\s]', '', url))
    features['unusual_character_ratio_url'] = features['special_count_url'] / features['url_length'] if features['url_length'] > 0 else 0
    
    # Content features
    features['count_dot_content'] = content.count('.')
    features['count%_content'] = content.count('%')
    features['count-_content'] = content.count('-')
    features['count=_content'] = content.count('=')
    features['sus_content'] = suspicious_words(content)
    features['count_digits_content'] = sum(c.isdigit() for c in content)
    features['count_letters_content'] = sum(c.isalpha() for c in content)
    features['content_length'] = len(content)
    features['is_encoded_content'] = int('%' in content.lower())
    features['special_count_content'] = len(re.sub(r'[a-zA-Z0-9\s]', '', content))
    
    return pd.DataFrame(features, index=[0])

def classify_request(features):
    model = pickle.load(open('model.pkl', 'rb'))
    return model.predict(features)

# Example usage:
url = "http://example.com/page?param=value"
content = "This is a sample content with some unusual characters like $%@#"
extracted_features = extract_features(url, content)
classification = classify_request(extracted_features)
print("Classification:", classification)
