import asyncio
import uvicorn
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from scanner.web.lightScan.scanner import scanModules
from scanner.web.balancedScan.scanner import scanBalanced
app = FastAPI()
port = 8080

class Requirements(BaseModel):
    url: str
    mode: str


@app.post("/scanner")
async def MainScanner(item: Requirements):
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

    if mode != "light" or mode!="balanced":
        return [{"response": "Mode not found."}]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)