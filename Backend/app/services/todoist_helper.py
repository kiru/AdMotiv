from todoist.api import TodoistAPI
import os


class TodoistAccess:

    def __init__(self, path = os.path.join(os.path.dirname(__file__), "..", "resources", "secrets", "todoist_token.txt")):#'../resources/secrets/todoist_token.txt'):
        with open(path, 'rb') as f:
            my_token = f.readline().decode("utf-8")
        self.api = TodoistAPI(my_token)
        self.api.sync()

    def get_all_tasks(self):
        self.sync()
        tasks = self.api.items.all()
        return tasks

    def sync(self):
        self.api.sync()

    def get_content(self, note):
        return note["content"]

    def get_all_content(self):
        tasks = self.get_all_tasks()
        return [self.get_content(task) for task in tasks]

    def get_tasks_info(self):
        tasks = self.get_all_tasks()
        return [(task["content"], task["due"]) for task in tasks]
