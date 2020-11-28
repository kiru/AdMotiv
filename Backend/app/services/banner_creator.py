import random

CATEGORIES = ["Motivational", "Todoist", "Calendar", "Picture", "Content-Related"]

def create_random_banner(size_x: int, size_y: int):
    category = random.choice(CATEGORIES)
    return "/get_image?x=" + str(size_x) + "&y=" + str(size_y) + "&category=" + str(category);

