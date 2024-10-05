import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()
port = 8080


@app.get("/hi")
def printing():
    print("Hi, Its working.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)