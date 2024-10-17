import asyncio
import uvicorn
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from scanner.web.lightScan.scanner import scanModules
from scanner.web.balancedScan.scanner import scanBalanced
from scanner.network.scanner import NetworkScanner, n_map

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://voltsec-io-main.vercel.app",
    "https://voltsec-io.com",
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers (Authorization, Content-Type, etc.)
)


port = 8080

class Requirements(BaseModel):
    url: str
    mode: str

def remove_duplicates(vulnerabilities):
    seen = set()
    unique_vulnerabilities = []
    for vuln in vulnerabilities:
        if vuln["name"] not in seen:
            unique_vulnerabilities.append(vuln)
            seen.add(vuln["name"])
    return unique_vulnerabilities

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
        results = remove_duplicates(combined)
        return results

    if mode == "deep":
        light = await scanModules(url)
        balanced = await scanBalanced(url)
        main = light + balanced
        results = remove_duplicates(main)
        return results


    if mode != "light" or mode!="balanced" or mode!="deep":
        return [{"response": "Mode not found."}]


@app.post("/networkScan")
async def NetworkScan(item: Requirements):
    unique_data = []
    seen_ips = set()
    req_item = item.model_dump()
    mode = req_item["mode"].lower()
    url = req_item["url"].lower()
    if req_item['url'] == "":
        return {"response": "Please provide, URL!"}
    if req_item['mode'] == "":
        return {"response": "please provide mode"}
    destructure = url.split("//")[-1:]
    scan = await NetworkScanner(param=destructure[0])
    for item in scan:
        for ip, details in item.items():
            if ip not in seen_ips:
                seen_ips.add(ip)
                unique_data.append(item)
    return unique_data



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)