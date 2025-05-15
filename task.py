from id_generator import IdGenerator

class Task:
    def __init__(self, title, description):
        self.id = IdGenerator.get_next_id("task")
        self.title = title
        self.description = description

    # оновлення опису
    def update_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f"Завдання: {self.title})"

    def get_type(self):
        return "Завдання"
