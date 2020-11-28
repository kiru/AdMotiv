import random

from PIL import Image, ImageDraw, ImageFont

from services.font_loader import get_Roboto_Font
from services.motivational_helper import get_motivational_quote
from services.message_generator import MessageGenerator
import os

def get_motivational_image(x_size: int, y_size: int, topic : str = None):
    quote = get_motivational_quote()
    return generate_image(quote['text'], x_size, y_size)

def get_picture_image(x_size: int, y_size: int, topic : str = None):
    base_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "images")
    all_files = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f))]

    picked_image = random.choice(all_files)
    img = Image.open(os.path.join(os.path.dirname(__file__), "..", "resources", "images", picked_image))

    if img.width / img.height > (x_size / y_size):
        newwidth = int(img.height * (x_size / y_size))
        newheight = img.height
    else:
        newwidth = img.width
        newheight = int(img.width / (x_size / y_size))
    cropped_img = img.crop((0.5 * (img.width - newwidth),
                     0.5 * (img.height - newheight),
                     0.5 * (img.width - newwidth) + newwidth,
                     0.5 * (img.height - newheight) + newheight))

    resized_img = cropped_img.resize((x_size, y_size), Image.BICUBIC)

    return resized_img

def get_todoist_image(x_size: int, y_size: int, topic : str = None):
    generator = MessageGenerator(topic)
    message = generator.generate_random_todoist_message()
    image = generate_image(message, x_size, y_size)
    return image


def get_content_image(x_size: int, y_size: int, topic : str = None):
    pass


def create_next_appointment_image():
    pass


def generate_image(text: str, x_size: int, y_size: int):
    img = Image.new('RGB', (x_size, y_size), color=(255, 255, 255))
    max_bbox_size_height = 0.8 * img.height
    max_bbox_size_width = 0.8 * img.width

    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, x_size, y_size], outline=(0,0,0), width=5)

    font_size = 100
    font = ImageFont.truetype(get_Roboto_Font(), font_size)
    text_width, text_height = d.multiline_textsize(text, font=font)

    while text_width > max_bbox_size_width or text_height > max_bbox_size_height:
        font_size = font_size - 1
        font = ImageFont.truetype(get_Roboto_Font(), font_size)
        text_width, text_height = d.multiline_textsize(text, font=font)

    text_height += int(text_height * 0.21)
    d.multiline_text(((x_size - text_width) / 2, (y_size - text_height) / 2), text=text, fill='black', font=font)
    return img

