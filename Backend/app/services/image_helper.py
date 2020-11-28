from PIL import Image, ImageDraw, ImageFont

from services.font_loader import get_Roboto_Font


def create_image(content: str, x_size: int, y_size: int):
    img = Image.new('RGB', (x_size, y_size), color = (255, 255, 255))
    font = ImageFont.truetype(get_Roboto_Font(), 14)

    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, x_size, y_size], outline=(0,0,0), width=5)

    w, h = d.textsize(content, font=font)
    h += int(h * 0.21)
    d.text(((x_size - w) / 2, (y_size - h) / 2), text=content, fill='black', font=font)

    #d.multiline_text((10,10), content, fill=(0,0,0))
    return img

