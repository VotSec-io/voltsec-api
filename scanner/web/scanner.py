# lib/modules
# import asyncio

# file modules imports
from .modules.sql import checkSqlInjection
from .modules.check_csrf import check_csrf
from .modules.directory_traversal import check_directory_traversal
from .modules.open_redirect import check_open_redirect
from .modules.xxs import checkXXS


# This function will contain all the scan modules available in modules and scan for venerabilities and return the results
async def scanModules(param: str):
    sql = await checkSqlInjection(url=param)
    csrf = await check_csrf(url=param)
    open = await check_open_redirect(url=param)
    dict = await check_directory_traversal(url=param)
    check = await checkXXS(url=param)
    return {"sql": sql, "csrf": csrf, "open_redirect": open, "directory_traversal": dict, "xxs": check}