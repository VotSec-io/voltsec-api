import requests
from scanner.web.schema import Schema


results_integration = Schema(
    name="Software and Data Integrity Failures",
    description="Missing or weak integrity controls, leading to tampered software or data.",
    level="High",
    remediation="Implement security headers like Content-Security-Policy, X-Content-Type-Options, and use code signing or hashes for software integrity."
)


async def check_integrity_failures(url: str) -> bool:
    response = requests.get(url)
    security_headers = ["Content-Security-Policy", "X-Content-Type-Options", "X-Frame-Options"]
    for header in security_headers:
        if header not in response.headers:
            return True  # Missing integrity-related security header
    return False