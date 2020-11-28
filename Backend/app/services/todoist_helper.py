from todoist.api import TodoistAPI


class TodoistAccess:

    def __init__(self, path = '../resources/secrets/todoist_token.txt'):
        with open(path, 'rb') as f:
            my_token = f.readline().decode("utf-8")
        print(my_token)
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
