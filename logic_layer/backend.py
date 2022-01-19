import asyncio
from typing import Dict
from logic_layer.connection import createdb, connection


async def getRandomQuote(noOfDocuments: int = 1) -> Dict:
    async for i in quoteCol.aggregate([{"$sample": {"size": noOfDocuments}}]):
        return i


if __name__ == "logic_layer.backend" or __name__=="__main__":
    #conn = asyncio.run(connection())
    conn = connection()
    quoteCol = createdb(conn, "DiscordBot", "Quotes")
