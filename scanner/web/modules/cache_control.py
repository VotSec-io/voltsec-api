import requests
from scanner.web.schema import Schema

cache_results = Schema(
    name="Cache-Control Misconfiguration",
    description="Improperly configured Cache-Control headers can lead to the caching of sensitive information, exposing it to unauthorized users or serving outdated content.",
    level="High",
    remediation="Use Cache-Control: no-store, no-cache, must-revalidate, private for sensitive endpoints and Cache-Control: public, max-age=31536000, immutable for static resources.",
)

async def cache_check(url: str) -> bool:
    response = requests.get(url)
    header = response.headers.get('Cache-Control')
    if "public" in header:
        return True
    return False