import re
import urllib.parse
import asyncio
import requests

from scanner.web.schema import Schema

csrf_results = Schema(
    name= "Cross-Site Request Forgery (CSRF)",
    description= "CSRF vulnerabilities allow an attacker to perform actions on behalf of an authenticated user without their consent.",
    level= "High",
    remediation= "Implement anti-CSRF tokens and ensure they are used in all state-changing operations."
)

# ever wonder why men's find soo tough to find G-spot of women😒? 
# Wanna get the easiest way to find Gspot and be a man? (Find answer in another file 🥺😂😂 atlest try to finnd here!)

async def check_csrf(url: str) -> bool:
    try:
        response = requests.get(url=url, cookies={'withCredentials': 'true'})
        has_csrf_token = (re.search(r'<input[^>]+name=["\']?_csrf["\']?', response.text, re.IGNORECASE) or
                          re.search(r'<meta[^>]+name=["\']?_csrf["\']?', response.text, re.IGNORECASE) or
                          re.search(r'<meta[^>]+name=["\']?csrf-token["\']?', response.text, re.IGNORECASE))
        return not has_csrf_token
    except Exception as error:
        print("Error checking for CSRF token:", error)
        return False

