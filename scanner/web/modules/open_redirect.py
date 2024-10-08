import requests

def check_open_redirect(url: str) -> bool:
    open_redirect_payloads = [
        'http://evil.com', 'https://evil.com', '//evil.com'
    ]
    
    for payload in open_redirect_payloads:
        try:
            response = requests.get(url + payload, allow_redirects=True)
            if payload in response.url:
                return True
        except requests.exceptions.RequestException:
            continue
    
    return False
