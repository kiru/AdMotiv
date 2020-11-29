import random

CATEGORIES = ["Content-todo", "Content-cal"]

def create_random_banner(size_x: int, size_y: int, topic : str):
    category = random.choice(CATEGORIES)
    return "/get_image?x_size=" + str(size_x) + "&y_size=" + str(size_y) + "&type_of_content=" + str(category) + "&topic=" + str(topic);

