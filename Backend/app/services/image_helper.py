from PIL import Image, ImageDraw


def create_image(content: str, x_size: int, y_size: int):
    img = Image.new('RGB', (x_size, y_size), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    ImageFont

    d.rectangle([0, 0, x_size, y_size], outline=(0,0,0), width=5)
    d.multiline_text((10,10), content, fill=(0,0,0))
    return img

