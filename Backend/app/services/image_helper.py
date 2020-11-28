from PIL import Image, ImageDraw


def create_image(content: str, ):
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10,10), str(content), fill=(255,255,0))
    return img

