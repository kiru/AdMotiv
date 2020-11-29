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

def get_calendar_image(x_size: int, y_size: int, topic : str = None):
    generator = MessageGenerator(topic)
    message = generator.generate_random_calendar_message()
    image = generate_image(message, x_size, y_size)
    return image

def get_content_image_calendar(x_size: int, y_size: int, topic : str = None):
    generator = MessageGenerator(topic)
    message = generator.generate_random_calendar_message()
    image = generate_content_image(message, x_size, y_size)
    return image

def get_content_image_todoist(x_size: int, y_size: int, topic : str = None):
    generator = MessageGenerator(topic)
    message = generator.generate_random_todoist_message()
    image = generate_content_image(message, x_size, y_size)
    return image

def generate_content_image(text : str, x_size: int, y_size: int):
    img = Image.open(os.path.join(os.path.dirname(__file__), "..", "resources", "images", "photo1.jpg"))
    max_bbox_size_height = 0.8 * img.height
    max_bbox_size_width = 0.8 * img.width

    d = ImageDraw.Draw(img)
    #d.rectangle([0, 0, x_size, y_size], outline=(0, 0, 0), width=5)

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


def create_next_appointment_image():
    pass


def wrap_text_uniform(text, n_lines):
    words = text.split(" ")
    def split(a, n):
        k, m = divmod(len(a), n)
        return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))
    return "\n".join(list(map(lambda l: " ".join(l), split(words, n_lines))))


def generate_image(text: str, x_size: int, y_size: int):
    img = Image.new('RGB', (x_size, y_size), color=(255, 255, 255))
    max_bbox_size_height = 0.9 * img.height
    max_bbox_size_width = 0.9 * img.width

    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, x_size, y_size], outline=(0,0,0), width=5)

    font_size = int(0.05 * (max_bbox_size_height + max_bbox_size_width) / 2)
    font = ImageFont.truetype(get_Roboto_Font(), font_size)
    text_width, text_height = d.multiline_textsize(text, font=font)

    wrapping = 1
    wrapped_text = text
    while text_width > max_bbox_size_width or text_height > max_bbox_size_height and wrapping <= 10:
        font_size = font_size - 1
        font = ImageFont.truetype(get_Roboto_Font(), font_size)
        wrapping += 1
        wrapped_text = wrap_text_uniform(text, wrapping)
        print(wrapping)
        print(wrapped_text)
        text_width, text_height = d.multiline_textsize(wrapped_text, font=font)

    text_height += int(text_height * 0.21)
    d.multiline_text(((x_size - text_width) / 2, (y_size - text_height) / 2), text=wrapped_text, align='center', fill='black', font=font)
    return img
