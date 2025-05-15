import re
from datetime import datetime
from id_generator import IdGenerator

class Student:
    def __init__(self, first_name, last_name, email, birth_date):
        self.id = IdGenerator.get_next_id("student")
        self.first_name = first_name
        self.last_name = last_name
        self.email = self._validate_email(email)
        self.birth_date = self._validate_birth_date(birth_date)
        self.enrolled_courses = {}  # {course_id: {lesson_id: progress}}
        self.progress = {}

    def _validate_email(self, email):
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if not email_pattern.match(email):
            raise ValueError("Невірний формат email")
        return email

    def _validate_birth_date(self, birth_date):
        try:
            return datetime.strptime(birth_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Невірний формат дати народження. Використовуйте РРРР-ММ-ДД")

    # + студент на курс
    def enroll_in_course(self, course_id):
        if course_id not in self.enrolled_courses:
            self.enrolled_courses[course_id] = {}

    #чи записаний студент
    def is_enrolled_in_course(self, course_id):
        return course_id in self.enrolled_courses


    def get_lesson_progress(self, course_id, lesson_id):
        return self.progress.get(course_id, {}).get(lesson_id, 0)

    # оновлення прогресу
    def update_progress(self, course_id, lesson_id, progress):
        if course_id not in self.progress:
            self.progress[course_id] = {}
        self.progress[course_id][lesson_id] = progress

    # отрим загальний прогрес
    def get_course_progress(self, course_id, course_lessons):
        if course_id not in self.enrolled_courses or not course_lessons:
            return 0

        total_progress = 0
        lesson_count = len(course_lessons)

        for lesson in course_lessons:
            total_progress += self.get_lesson_progress(course_id, lesson.id)

        return total_progress / lesson_count if lesson_count > 0 else 0

    # отрим айді курсів на які записаний студент
    def get_enrolled_courses(self):
        return list(self.enrolled_courses.keys())

    def __str__(self):
        return f"Студент: {self.first_name} {self.last_name} ({self.email})"
