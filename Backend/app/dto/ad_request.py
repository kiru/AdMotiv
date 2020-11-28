from typing import List

from pydantic import BaseModel


class AdRequest(BaseModel):
    title: str
    content: str
    banners: List[List[int]]