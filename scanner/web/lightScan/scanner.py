# lib/modules
# import asyncio

# file modules imports
from ..modules.check_csrf import check_csrf, csrf_results
from ..modules.directory_traversal import check_directory_traversal, dire_results
from ..modules.sql import checkSqlInjection, results_sql
from ..modules.open_redirect import check_open_redirect, results_redirect
from ..modules.xxs import checkXXS, results_xxs
from ..modules.securityHeaders import check_security_headers
from ..modules.server_reveal import server_results, server_reveal_check
from ..modules.http_methods_override import check_http_override, override_results
from ..modules.cache_control import cache_results, cache_check

response = []

# This function will contain all the scan modules available in modules and scan for venerabilities and return the results
async def scanModules(param: str):
    sql = await checkSqlInjection(url=param)
    csrf = await check_csrf(url=param)
    open_redirect = await check_open_redirect(url=param)
    directory_traversal = await check_directory_traversal(url=param)
    xxs = await checkXXS(url=param)
    http_override = await check_http_override(url=param)
    server_check = await server_reveal_check(url=param)
    cache = await cache_check(url=param)
    security_headers = await check_security_headers(url=param)

    if sql:
        response.append(results_sql)
    if csrf:
        response.append(csrf_results)
    if directory_traversal:
        response.append(dire_results)
    if open_redirect:
        response.append(results_redirect)
    if xxs:
        response.append(results_xxs)
    if http_override:
        response.append(override_results)
    if server_check:
        response.append(server_results)
    if cache:
        response.append(cache_results)
    if security_headers!=[]:
        for headers in security_headers:
            response.append(headers)
    
    return response