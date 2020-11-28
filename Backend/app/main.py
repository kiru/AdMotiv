import io
from typing import Optional, List

from fastapi import FastAPI, status
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from dto.ad_request import AdRequest
from services.banner_creator import create_random_banner
from services.image_helper import get_motivational_image, get_picture_image, get_todoist_image, \
    get_content_image

app = FastAPI()


@app.post("/get_ad_replacement", status_code=status.HTTP_200_OK)
async def get_ad_replacement(ad_request: AdRequest):
    response = {"banners": []}
    for banner in ad_request.banners:
        response["banners"].append(create_random_banner(banner[0], banner[1]))
    return response


@app.get("/get_image", status_code=status.HTTP_200_OK)
async def get_image(x_size: int, y_size: int, type_of_content: str):

    switcher = {
        "Motivational": get_motivational_image,
        "Todoist": get_todoist_image,
        "Picture": get_picture_image,
        "Content-Related": get_content_image
    }

    function_call = switcher.get(type_of_content)
    img = function_call(x_size, y_size)

    output = io.BytesIO()
    img.save(output, format="png")
    output.seek(0)
    img.close()

    return StreamingResponse(output, media_type="image/png")


@app.get("/")
async def root():
    return {"message": "Hello World"}