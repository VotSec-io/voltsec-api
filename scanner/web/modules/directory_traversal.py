import requests
import re


# sometimes you saw her, you go and touch her, you even try to go forward but suddenly your alarm rang! 
# groSS!! worst moment


def check_directory_traversal(url: str) -> bool:
    traversal_payloads = [
        '../../../../etc/passwd', '..%2F..%2F..%2F..%2Fetc%2Fpasswd'
    ]
    
    for payload in traversal_payloads:
        try:
            response = requests.get(url + payload)
            if re.search(r'root:', response.text):
                return True
        except requests.exceptions.RequestException:
            continue
    
    return False
