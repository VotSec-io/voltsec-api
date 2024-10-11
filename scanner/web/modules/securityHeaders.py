import requests

from scanner.web.schema import Schema

headers = [
    Schema(
        "Content-Security-Policy", 
        "The Content-Security-Policy header helps prevent cross-site scripting (XSS) attacks.", 
        "High", 
        "Set a strict Content-Security-Policy header."),
    Schema(
        "X-Content-Type-Options", 
        "The X-Content-Type-Options header prevents MIME type sniffing.", 
        "Medium", 
        "Set the X-Content-Type-Options header to 'nosniff'."),
    Schema(
        "X-Frame-Options", 
        "The X-Frame-Options header protects against clickjacking attacks.", 
        "Medium", 
        "Set the X-Frame-Options header to 'DENY' or 'SAMEORIGIN'."),
    Schema(
        "X-XSS-Protection", 
        "The X-XSS-Protection header enables the cross-site scripting filter built into most browsers.", 
        "Low", 
        "Set the X-XSS-Protection header to '1; mode=block'."),
    Schema(
        "Strict-Transport-Security", 
        "The Strict-Transport-Security header enforces secure (HTTP over SSL/TLS) connections to the server.", 
        "High", 
        "Set the Strict-Transport-Security header to 'max-age=31536000; includeSubDomains'."),
    Schema(
        "Referrer-Policy", 
        "The Referrer-Policy header controls how much referrer information is included with requests.", 
        "Low", 
        "Set the Referrer-Policy header to 'no-referrer' or 'same-origin'."),
    Schema(
        "Permissions-Policy", 
        "The Permissions-Policy header controls which features and APIs can be used in the browser.", 
        "Medium", 
        "Set the Permissions-Policy header to restrict feature usage.")
]

async def check_security_headers(url: str):
    response = requests.get(url)

    # Filter headers that are either missing or have empty values in the response
    missing_headers = [
        header for header in headers
        if header.name.lower() not in response.headers or response.headers[header.name.lower()] == ''
    ]

    # Create a list of dictionaries containing the details of missing headers
    results = [
        {
            "name": header.name,
            "description": header.description,
            "level": header.level,
            "remediation": header.remediation
        } for header in missing_headers
    ]
    
    return results
