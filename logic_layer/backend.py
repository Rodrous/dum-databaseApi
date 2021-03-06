from typing import Dict, List, Union, Optional, Any
import os
import motor.motor_asyncio
from dotenv import load_dotenv


def create_db(connectionobj, databasename, collectionname) -> Any:
    db = connectionobj[databasename]
    collection = db[collectionname]
    return collection


async def add_quote(movie: str, character: str,
                    quote: List[List[Union[str, Optional[Dict[str, bool]]]]],
                    type_: str,
                    imageUrl: Optional[str] = None) -> None:
    check_existing = await quoteCol.count_documents({"$and": [
        {"movie": movie},
        {"character": character},
        {"quote": {"$elemMatch": {"$elemMatch": {"$eq": quote}}}}
    ]
    }
    )

    if check_existing == 0:
        await quoteCol.insert_one({
            "movie": movie,
            "character": character,
            "quote": quote,
            "imageurl": imageUrl,
            "type": type_

        })
    else:
        await quoteCol.update_one(
            {"$and": [
                {
                    "movie": movie
                }, {
                    "character": character
                }
            ]
            },
            {
                "$addToSet": {
                    "quote": {
                        "$each": quote
                    }
                }
            }
        )


async def add_descriptions(description: str) -> None:
    await description_cursor.update_one({
        "description": description
    },
        {"$setOnInsert": {"description": description}},
        upsert=True
    )


async def add_waiting_message(message: str) -> None:
    await loading_Message.update_one({"message": message},
                                     {"$setOnInsert": {"message": message}},
                                     upsert=True)


async def update_quote_image(movie: str, imageurl: str) -> None:
    await quoteCol.update_one({
        "movie": movie
    },
        {
            "$set": {"imageurl": imageurl}
        })


async def get_random_quote(noOfDocuments: int = 1) -> Dict:
    async for i in quoteCol.aggregate([{"$sample": {"size": noOfDocuments}}, {"$project": {"_id": 0}}]):
        return i


async def get_random_loading_message(noOfDocuments: int = 1) -> str:
    async for i in loading_Message.aggregate([{"$sample": {"size": noOfDocuments}}]):
        return i["message"]


async def get_random_description(noOfDescription: int = 1) -> str:
    async for i in description_cursor.aggregate([{"$sample": {"size": noOfDescription}}]):
        return i["description"]


async def authenticateUser(userName: str) -> Optional[str]:
    userInfo = await authentication.find_one({
        "user": userName
    },
    {"_id":0}
    )
    if userInfo:
        return userInfo["password"]


if __name__ == "logic_layer.backend":
    load_dotenv()
    client: str = os.environ.get("mongoDb")
    conn = motor.motor_asyncio.AsyncIOMotorClient(client)

    quoteCol = create_db(conn, "DiscordBot", "Quotes")
    loading_Message = create_db(conn, "DiscordBot", "LoadingMessage")
    description_cursor = create_db(conn, "DiscordBot", "Description")
    authentication = create_db(conn, "DiscordBot", "authenticate")
