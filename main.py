#!/usr/bin/python3
from typing import Dict

import uvicorn
from fastapi import FastAPI

from logic_layer.backend import getRandomQuote

app: FastAPI = FastAPI()

@app.get("/")
async def index() -> Dict:
    return {
        "Hello": "World!"
    }

@app.get("/randomQuote")
async def getQuote() -> Dict:
    x = await getRandomQuote()
    someDict:Dict = {
        "movie": x["movie"],
        "character": x["character"],
        "quote": x["quote"]
    }
    return someDict
