from id_generator import IdGenerator

class Course:
    def __init__(self, title, description):
        self.id = IdGenerator.get_next_id("course")
        self.title = title
        self.description = description
        self.lessons = []
        self.enrolled_students = set()

    # + студент
    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    # отрим заняття за айді
    def get_lesson_by_id(self, lesson_id):
        for lesson in self.lessons:
            if lesson.id == lesson_id:
                return lesson
        return None

    # + студент на курс
    def enroll_student(self, student_id):
        self.enrolled_students.add(student_id)

    # чи записаний студент на курс
    def is_student_enrolled(self, student_id):
        return student_id in self.enrolled_students

    # записані студенти
    def get_enrolled_students_count(self):
        return len(self.enrolled_students)

    def __str__(self):
        return f"Курс: {self.title} - {self.description} ({len(self.lessons)} занять)"