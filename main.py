#!/usr/bin/python3
from typing import Dict

from fastapi import FastAPI
from helpers.helperClasses import QuoteRequestStruct, AddDescription, AddLoadingMessage, UpdateQuoteImage
from logic_layer.backend import add_quote, add_descriptions, update_quote_image

app: FastAPI = FastAPI()


@app.get("/")
async def index() -> Dict:
    return {
        "Hello": "World!"
    }


@app.put("/addQuote/")
async def add_new_quote(input_body: QuoteRequestStruct) -> Dict:
    #await add_quote(input_body.dict())
    return input_body.dict()


@app.put("/addDescription")
async def add_new_description(input_body: AddDescription) -> Dict:
    #await add_descriptions(input_body.dict())
    return input_body.dict()


@app.put("/addWaitingMessage")
async def add_waiting_message(input_body: AddLoadingMessage) -> Dict:
    #await add_waiting_message(input_body.dict())
    return input_body.dict()


@app.put("/updateQuoteImage")
async def update_quote(input_body: UpdateQuoteImage) -> Dict:
    #await update_quote_image(input_body.dict())
    return input_body.dict()
