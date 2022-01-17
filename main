#!/usr/bin/python3
from typing import Dict

from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/")
async def index() -> Dict:
    return {
        "Hello": "World!"
    }
