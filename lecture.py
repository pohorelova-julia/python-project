from id_generator import IdGenerator

class Lecture:
    def __init__(self, title, content):
        self.id = IdGenerator.get_next_id("lecture")
        self.title = title
        self.content = content

    # оновлення занять
    def update_content(self, new_content):
        self.content = new_content

    def __str__(self):
        return f"Лекція: {self.title}"

    def get_type(self):
        return "Лекція"
