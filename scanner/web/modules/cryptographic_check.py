import requests
from scanner.web.schema import Schema

crypto_results = Schema(
    name="Cryptographic Failures",
    description="Inadequate encryption or lack of HTTPS, exposing sensitive data.",
    level="High",
    remediation="Enforce HTTPS, use strong encryption algorithms (e.g., AES-256), and ensure proper key management."
)


async def check_cryptographic_failures(url: str) -> bool:
    response = requests.get(url)
    if not url.startswith("https"):
        return True  # No HTTPS, cryptographic failure
    if "Strict-Transport-Security" not in response.headers:
        return True  # Missing HSTS header, possible issue
    return False