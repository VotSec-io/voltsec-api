import requests
from scanner.web.schema import Schema

week_auth_results = Schema(
    name="Identification and Authentication Failures",
    description="Weak or misconfigured authentication systems (e.g., default passwords, no multi-factor authentication).",
    level="High",
    remediation="Enforce strong password policies, use multi-factor authentication (MFA), and ensure secure session management."
)


async def check_authentication_failures(url: str) -> bool:
    default_login_paths = ["/login", "/signin", "/admin/login"]
    for path in default_login_paths:
        response = requests.get(url + path)
        if response.status_code == 200:
            return True  # Possible weak authentication mechanisms
    return False
