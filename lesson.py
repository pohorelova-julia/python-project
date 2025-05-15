from id_generator import IdGenerator

class Lesson:
    def __init__(self, title):
        self.id = IdGenerator.get_next_id("lesson")
        self.title = title
        self.content = []  # міститиvt Lecture та Task

    # + лекція/завдання
    def add_content(self, content_item):
        self.content.append(content_item)

    # отрим лекцій
    def get_lectures(self):
        from lecture import Lecture
        return [item for item in self.content if isinstance(item, Lecture)]

    # отрим завдань
    def get_tasks(self):
        from task import Task
        return [item for item in self.content if isinstance(item, Task)]

    def __str__(self):
        return f"Заняття: {self.title} ({len(self.content)} елементів вмісту)"
