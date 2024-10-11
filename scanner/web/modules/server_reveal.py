import requests
from scanner.web.schema import Schema

server_results = Schema(
    name="Server Header",
    description="The Server header reveals the web server type and version, exposing the stack to potential targeted attacks.",
    level="Low",
    remediation="Mainly an information disclosure issue, but it can increase the risk of targeted attacks based on the server's version or softwar."
)


async def server_reveal_check(url: str) -> bool:
    response = requests.get(url)
    
    if 'server' or 'Server' in response.headers:
        return True
    return False