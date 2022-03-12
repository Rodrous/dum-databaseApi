#!/usr/bin/python3

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette import status

from helpers.helperClasses import QuoteRequestStruct, AddDescription, AddLoadingMessage, UpdateQuoteImage
from helpers.securityCheck import UserInfoVerification
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.get("/")
async def index():
    return RedirectResponse("https://www.youtube.com/watch?v=xvFZjo5PgG0")


@app.put("/addQuote/")
async def add_new_quote(input_body: QuoteRequestStruct, token: str = Depends(oauth2_scheme)) -> None:
    await add_quote(input_body.movie,
                    input_body.character,
                    input_body.quote,
                    input_body.type,
                    input_body.imageUrl,
                    )


@app.put("/addDescription")
async def add_new_description(input_body: AddDescription, token: str = Depends(oauth2_scheme)) -> None:
    await add_descriptions(input_body.description)


@app.put("/addWaitingMessage")
async def waiting_message(input_body: AddLoadingMessage, token: str = Depends(oauth2_scheme)) -> None:
    await add_waiting_message(input_body.loadingMessage)


@app.put("/updateQuoteImage")
async def quote_image_update(input_body: UpdateQuoteImage, token: str = Depends(oauth2_scheme)) -> None:
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


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    verify = UserInfoVerification(form_data.username, form_data.password)
    verify = await verify.authenticate()
    if not verify:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": form_data.username, "token_type": "bearer"}
