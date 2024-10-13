import requests
from scanner.web.schema import Schema

results_broken = Schema(
    name="Broken Access Control",
    description="Unauthorized access to restricted resources (e.g., admin panels, sensitive data).",
    level="Critical",
    remediation="Implement proper role-based access control (RBAC) and ensure strict permissions for sensitive endpoints."
)


async def check_broken_access(url: str) -> bool:
    sensitive_paths = ["/admin", "/dashboard", "/settings", "/secret"]
    for path in sensitive_paths:
        response = requests.get(url + path)
        if response.status_code == 200:
            return True  # Potential broken access control
    return False