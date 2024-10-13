import asyncio

from ..modules.broken_access import check_broken_access, results_broken
from ..modules.vulnerable_components import check_vulnerable_components, vulreable_results
from ..modules.week_auth import check_authentication_failures, week_auth_results
from ..modules.cryptographic_check import check_cryptographic_failures, crypto_results
from ..modules.integration_failure import check_integrity_failures, results_integration
from ..modules.ssrf import check_ssrf, ssrf

response = []

async def scanBalanced(param: str):
    brokenAccess = await check_broken_access(url=param)
    vulnerable = await check_vulnerable_components(url=param)
    weekAuth = await check_authentication_failures(url=param)
    crypto = await check_cryptographic_failures(url=param)
    integration = await check_integrity_failures(url=param)
    ssrf_check = await check_ssrf(url=param)

    if brokenAccess:
        response.append(results_broken)
    if vulnerable:
        response.append(vulreable_results)
    if weekAuth:
        response.append(week_auth_results)
    if crypto:
        response.append(crypto_results)
    if integration:
        response.append(results_integration)
    if ssrf_check:
        response.append(ssrf)
    return response