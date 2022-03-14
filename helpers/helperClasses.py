from typing import List, Union, Optional, Dict

from pydantic import BaseModel, HttpUrl


class QuoteRequestStruct(BaseModel):
    movie: str
    character: str
    quote: List[List[Union[str, Optional[Dict[str, bool]]]]]
    imageUrl: Optional[str]
    type: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "movie": "Naruto Shippuden",
                "character": "Madara Uchiha",
                "quote": [
                    [
                        "The Uchiha is a clan destined for revenge.",
                        {
                            "Explicit": False,
                            "NSFW": False
                        }
                    ],
                    [
                        "Wake up to reality! Nothing ever goes as planned in this world. "
                        "The longer you live, the more you realize that in this reality, only pain, suffering, "
                        "and futility exist.",
                        {
                            "Explicit": False,
                            "NSFW": False
                        }
                    ]

                ],
                "imageurl": "https://qph.fs.quoracdn.net/main-qimg-7dc4c8f9e9ff57f38050cc54940a012e",
                "type": "Quote"

            }
        }


class AddDescription(BaseModel):
    description: str


class AddLoadingMessage(BaseModel):
    loadingMessage: str


class UpdateQuoteImage(BaseModel):
    movie: str
    imageUrl: str
