from todoist.api import TodoistAPI


class Todoist_acess:



    def __init__(self, my_token = "98083af007fffeddb55984923076c70c3f84bcb7"):
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
