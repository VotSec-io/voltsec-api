import asyncio

from .modules.nmap import n_map


async def NetworkScanner(param):
    Nmap = await n_map(url=param)
    return Nmap