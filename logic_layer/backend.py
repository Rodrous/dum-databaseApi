from typing import Dict, List, Union, Optional, Any
import os
import motor.motor_asyncio
from dotenv import load_dotenv


def createdb(connectionobj, databasename, collectionname) -> Any:
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
    await Loading_Message.update_one({"message": message},
                                     {"$setOnInsert": {"message": message}},
                                     upsert=True)


async def update_quote_image(movie: str, imageurl: str) -> None:
    await quoteCol.update_one({
        "movie": movie
    },
        {
            "$set": {"imageurl": imageurl}
        })


if __name__ == "logic_layer.backend":
    load_dotenv()
    client: str = os.environ.get("mongoDb")
    conn = motor.motor_asyncio.AsyncIOMotorClient(client)

    # Connection cursors start from here
    quoteCol = createdb(conn, "DiscordBot", "Quotes")
    Loading_Message = createdb(conn, "DiscordBot", "Loading_Message")
    description_cursor = createdb(conn, "DiscordBot", "Description")
