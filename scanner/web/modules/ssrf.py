import requests
from scanner.web.schema import Schema

ssrf = Schema(
    name="Server-Side Request Forgery (SSRF)",
    description="Attackers can send malicious requests from the server to internal services or external resources.",
    level="High",
    remediation="Restrict server-side requests to trusted resources, validate URLs, and block requests to internal or private IPs."
)


async def check_ssrf(url: str) -> bool:
    ssrf_test_ips = ["http://127.0.0.1", "http://169.254.169.254"]  # Localhost or AWS Metadata URL
    for test_ip in ssrf_test_ips:
        try:
            response = requests.get(f"{url}?test={test_ip}")
            if response.status_code == 200:
                return True  # SSRF vulnerability
        except:
            pass  # Ignore connection errors
    return False