# distributed-demo/app/main.py
from fastapi import FastAPI, Request
import os
import socket

app = FastAPI()
# instance id from env variable or hostname
INSTANCE_ID = os.getenv("INSTANCE_ID", socket.gethostname())

@app.get("/")
async def root(request: Request):
    # return instance id and client's remote ip
    return {
        "instance": INSTANCE_ID,
        "path": str(request.url.path),
        "message": "Hello from distributed server demo"
    }

@app.get("/health")
async def health():
    return {"status": "ok", "instance": INSTANCE_ID}
