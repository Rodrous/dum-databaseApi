#!/usr/bin/python3

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from helpers.helperClasses import QuoteRequestStruct, AddDescription, AddLoadingMessage, UpdateQuoteImage
from logic_layer.backend import add_quote, add_descriptions, update_quote_image, add_waiting_message, get_random_quote, \
    get_random_loading_message, get_random_description

app: FastAPI = FastAPI(
    title="Database API",
    version="0.0.1",
    description="""
   
   This basically contains the methods the webapp will use to insert 
   specific items in Database which is used by the bot ☁️
    """,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}

)


@app.get("/")
async def index():
    return RedirectResponse("https://www.youtube.com/watch?v=xvFZjo5PgG0")


@app.put("/addQuote/")
async def add_new_quote(input_body: QuoteRequestStruct) -> None:
    await add_quote(input_body.movie,
                    input_body.character,
                    input_body.quote,
                    input_body.type,
                    input_body.imageUrl,
                    )


@app.put("/addDescription")
async def add_new_description(input_body: AddDescription) -> None:
    await add_descriptions(input_body.description)


@app.put("/addWaitingMessage")
async def waiting_message(input_body: AddLoadingMessage) -> None:
    await add_waiting_message(input_body.loadingMessage)


@app.put("/updateQuoteImage")
async def quote_image_update(input_body: UpdateQuoteImage) -> None:
    await update_quote_image(input_body.movie, input_body.imageUrl)


@app.get("/getRandomQuote")
async def random_quote():
    return await get_random_quote()


@app.get("/getRandomLoadingMessage")
async def random_loading_message() -> str:
    return await get_random_loading_message()


@app.get("/getRandomDescription")
async def random_description() -> str:
    return await get_random_description()
