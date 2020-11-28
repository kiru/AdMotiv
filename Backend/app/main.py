import io

from fastapi import FastAPI, status
from starlette.responses import StreamingResponse

from services.image_helper import create_image

app = FastAPI()



@app.post("/ad_replacement", status_code=status.HTTP_200_OK)
async def get_add_replacement(content: str):
    pass



@app.post("/get_image", status_code=status.HTTP_200_OK)
async def get_image(x_size: int, y_size: int):
    img = create_image(x_size, y_size)

    output = io.BytesIO()
    img.save(output, format="png")
    output.seek(0)
    img.close()

    return StreamingResponse(output, media_type="image/png")


@app.get("/")
async def root():
    return {"message": "Hello World"}