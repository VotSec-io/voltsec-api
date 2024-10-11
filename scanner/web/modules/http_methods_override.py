import requests
from scanner.web.schema import Schema

override_results = Schema(
    name="HTTP Method Overriding",
    description="Allows overriding of HTTP methods (e.g., POST to DELETE) using headers like X-HTTP-Method-Override, potentially bypassing method restrictions",
    level="High",
    remediation="Disable or restrict method overriding unless absolutely necessary. Validate allowed methods server-side."
)
async def check_http_override(url: str) -> bool:
    headers = {'X-HTTP-Method-Override': 'DELETE'}
    response = requests.post(url, headers=headers)

    if response.status_code == [200, 204, 405]:
        return True
    return False 