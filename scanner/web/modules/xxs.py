# kabhi kabhi dil me khayal aata hai.. na jane kya rakha hai duniya dari me, ladki me...
# kas ye khayal hilane ke phele aa jata.

import re
import urllib.parse
import requests
from scanner.web.schema import Schema

results_xxs = Schema(
    name= "Cross-Site Scripting (XSS)",
    description= "XSS vulnerabilities allow an attacker to inject malicious scripts into web pages viewed by other users.",
    level= "Medium",
    remediation= "Escape user input and use Content Security Policy (CSP) to prevent XSS attacks."
)

async def checkXXS(url: str) -> bool:
    xss_payloads = [
        "<script>alert('XSS')</script>", 
        "<img src='x' onerror='alert(1)'>", 
        "<svg onload='alert(1)'>"
    ]
    
    # Check each XSS payload
    for payload in xss_payloads:
        # Encode the payload properly
        encoded_payload = urllib.parse.quote(payload)
        full_url = urllib.parse.urljoin(url, encoded_payload)

        try:
            # Send the request to the server
            response = requests.get(full_url)
            
            # Check if the payload is reflected in the response body
            if response.status_code == 200 and re.search(re.escape(payload), response.text):
                return True

        except requests.exceptions.RequestException as e:
            print(f"Error during request: {e}")
            continue
    
    return False


# wahhh! gspot ki itni talab ki yaha tk pooch gaye chalo dekh lo fir...

# fir in the pussy above the hole you will find something called "clit"
# aab chutiyo ke tara ye maat poochna clit kya hota hai google kr lo. 😑
# hole ke barabr uper dot sa hoga kush reh...
# usko aise touch kro jaise feather ho.. usko halka halka sa hilo 
# na zada tezz na zada halka... bohot aarm se taki usko pleasure mile

# lo bdsk hit kr liya gspot itna tk tumara nahi nikla to kr lena aage ka karikram