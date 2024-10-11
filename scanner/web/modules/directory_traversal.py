import requests
import urllib
import urllib.parse
import re

from scanner.web.schema import Schema

# sometimes you saw her, you go and touch her, you even try to go forward but suddenly your alarm rang! 
# groSS!! worst moment

dire_results = Schema(
    name= "Directory Traversal",
    description= "Directory traversal vulnerabilities allow attackers to access files and directories outside the intended directory.",
    level= "High",
    remediation= "Validate and sanitize all user inputs, and use secure APIs to access the file system."
)

async def check_directory_traversal(url: str) -> bool:
    traversal_payloads = [
        '../../../../etc/passwd', '..%2F..%2F..%2F..%2Fetc%2Fpasswd'
    ]
    for payload in traversal_payloads:
        try:
            response = requests.get(url)
            if re.search(r'root:', response.text):
                return True
        except requests.exceptions.RequestException:
            continue
    
    return False
