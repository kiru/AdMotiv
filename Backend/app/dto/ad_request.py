from typing import List

from pydantic import BaseModel


class Image(BaseModel):
    height: int
    width: int

class AdRequest(BaseModel):
    title: str
    content: str
    banners: List[Image]