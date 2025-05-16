from id_generator import IdGenerator
from lecture import Lecture
from task import Task

class Lesson:
    def __init__(self, title):
        self.id = IdGenerator.get_next_id("lesson")
        self.title = title
        self.content = []  # міститиме об'єкти Lecture та Task

    # + лекція/завдання
    def add_content(self, content_item):
        self.content.append(content_item)

    # отрим лекцій
    def get_lectures(self):
        lectures = []
        for item in self.content:
            if isinstance(item, Lecture):
                lectures.append(item)
        return lectures

    # отрим завдань
    def get_tasks(self):
        tasks = []
        for item in self.content:
            if isinstance(item, Task):
                tasks.append(item)
        return tasks

    def __str__(self):
        return f"Заняття: {self.title} ({len(self.content)} елементів вмісту)"
