import io
from typing import Optional, List

from fastapi import FastAPI, status
from starlette.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from services.html_dom import extract_text_from_dom
from services.nlp_few_shot_classifier import classify_text_into_keyword

from dto.ad_request import AdRequest
from services.banner_creator import create_random_banner
from services.image_helper import get_motivational_image, get_picture_image, get_todoist_image, \
    get_content_image_calendar, get_content_image_todoist, get_calendar_image

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/get_ad_replacement", status_code=status.HTTP_200_OK)
async def get_ad_replacement(ad_request: AdRequest):
    response = {"banners": []}

    html_body = ad_request.content
    key_words = extract_text_from_dom(html_body)
    topic = classify_text_into_keyword(" ".join(key_words[:10]))

    for banner in ad_request.banners:
        response["banners"].append({
            "id": banner.id,
            "url": create_random_banner(banner.width, banner.height, topic)
        })
    return response


@app.get("/get_image", status_code=status.HTTP_200_OK)
async def get_image(x_size: int, y_size: int, type_of_content: str, topic : str):

    if y_size >= 2 * x_size:
        type_of_content = "Picture"

    switcher = {
        "Motivational": get_motivational_image,
        "Todoist": get_todoist_image,
        "Picture": get_picture_image,
        "Content-todo": get_content_image_todoist,
        "Content-cal": get_content_image_calendar,
        "Calendar": get_calendar_image
    }

    function_call = switcher.get(type_of_content)
    img = function_call(x_size, y_size, topic)

    output = io.BytesIO()
    img.save(output, format="png")
    output.seek(0)
    img.close()

    return StreamingResponse(output, media_type="image/png")


@app.get("/")
async def root():
    return {"message": "Hello World"}