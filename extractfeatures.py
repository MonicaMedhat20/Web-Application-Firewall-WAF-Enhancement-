import requests

def extract_headers_from_url(url):
    try:
        response = requests.head(url)  # Send a HEAD request to fetch headers only
        headers = {
            'Method': response.request.method,
            'User-Agent': response.request.headers.get('User-Agent'),
            'Pragma': response.request.headers.get('Pragma'),
            'Cache-Control': response.request.headers.get('Cache-Control'),
            'Accept': response.request.headers.get('Accept'),
            'Accept-Encoding': response.request.headers.get('Accept-Encoding'),
            'Accept-Charset': response.request.headers.get('Accept-Charset'),
            'Language': response.request.headers.get('Language'),
            # 'Host': response.request.headers.get('Host'),
            'Cookie': response.request.headers.get('Cookie'),
            'Content-Type': response.request.headers.get('Content-Type'),
            'Connection': response.request.headers.get('Connection'),
            'Length': response.headers.get('Content-Length'),
            'Content': None  # Content is not included in the headers, it's in the response body
        }
        return headers
    except requests.exceptions.RequestException as e:
        print("Error fetching headers:", e)
        return None

# Example usage
url= "http://localhost:8080/tienda1/miembros/editar.jsp"
headers = extract_headers_from_url(url)
if headers:
    print("Extracted Headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")
