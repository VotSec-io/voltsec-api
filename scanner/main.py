import asyncio
import uvicorn
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from scanner.web.lightScan.scanner import scanModules
from scanner.web.balancedScan.scanner import scanBalanced

from scanner.network.scanner import NetworkScanner, n_map

app = FastAPI()
port = 8080

class Requirements(BaseModel):
    url: str
    mode: str


@app.post("/scanner")
async def WebScanner(item: Requirements):
    item_dict = item.model_dump()
    url = item_dict["url"].lower()
    mode = item_dict['mode'].lower()
    if item_dict['url'] == "":
        return {"response": "Please provide, URL!"}
    if item_dict['mode'] == "":
        return {"response": "please provide mode"}
    if mode == "light":
        scan = await scanModules(url)
        return scan

    if mode == "balanced":
        light = await scanModules(url)
        balanced = await scanBalanced(url)
        combined = light + balanced
        return combined

    if mode == "deep":
        light = await scanModules(url)
        balanced = await scanBalanced(url)
        
        main = light + balanced
        return main

    if mode != "light" or mode!="balanced" or mode!="deep":
        return [{"response": "Mode not found."}]


@app.post("/networkScan")
async def NetworkScan(item: Requirements):
    req_item = item.model_dump()
    mode = req_item["mode"].lower()
    url = req_item["url"].lower()
    if req_item['url'] == "":
        return {"response": "Please provide, URL!"}
    if req_item['mode'] == "":
        return {"response": "please provide mode"}
    destructure = url.split("//")[-1:]
    scan = await NetworkScanner(param=destructure[0])
    return scan



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)