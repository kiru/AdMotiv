import random

CATEGORIES = ["Motivational", "Todoist", "Calendar", "Picture", "Content-Related"]

def create_random_banner(size_x: int, size_y: int):
    category = random.choice(CATEGORIES)
    return "/get_image?x_size=" + str(size_x) + "&y_size=" + str(size_y) + "&type_of_content=" + str(category);

