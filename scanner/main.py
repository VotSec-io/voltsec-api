import os
import uvicorn
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
port = 8080

class Requirements(BaseModel):
    url: str
    mode: str


@app.post("/scanner")
def printing(item: Requirements):
    if item.url == "":
        return {"response": "Please provide, URL!"}
    if item.mode == "":
        return {""}
    
    item_dict = item.model_dump()
    return [item_dict]
    # return {"response": f"{item.url}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)