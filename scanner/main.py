import asyncio
import uvicorn
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from web.scanner import scanModules
app = FastAPI()
port = 8080

class Requirements(BaseModel):
    url: str
    mode: str


@app.post("/scanner")
async def lightScan(item: Requirements):
    item_dict = item.model_dump()
    url = item_dict["url"].lower()
    mode = item_dict['mode'].lower()
    if item_dict['url'] == "":
        return {"response": "Please provide, URL!"}
    if item_dict['mode'] == "":
        return {"response": "please provide mode"}
    if mode == "light":
        scan = await scanModules(item_dict["url"])
        return [scan]
    if mode != "light":
        return [{"response": "Other modes are on development!"}]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)