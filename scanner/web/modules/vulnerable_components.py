import requests
from scanner.web.schema import Schema

vulreable_results = Schema(
    name="Vulnerable and Outdated Components",
    description="Using outdated libraries or components with known vulnerabilities.",
    level="High",
    remediation="Regularly update software dependencies, use tools like OWASP Dependency-Check, and monitor for security patches."
)


async def check_vulnerable_components(url: str) -> bool:
    """
    Check for outdated components by examining common CMS patterns or known vulnerable libraries.
    """
    known_vulnerable_paths = ["/wp-admin", "/wp-content", "/joomla", "/drupal"]
    for path in known_vulnerable_paths:
        response = requests.get(url + path)
        if response.status_code == 200:
            return True  # Possible vulnerable component
    return False