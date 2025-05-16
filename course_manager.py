from course import Course
from lesson import Lesson
from lecture import Lecture
from task import Task
from student import Student
from validators import Validators


class CourseManager:
    def __init__(self):
        self.courses = {}
        self.students = {}
        self.validators = Validators()

    def load_sample_data(self):
        # + курси
        python_course = Course("Програмування на Python", "Вивчіть Python з нуля")
        web_dev_course = Course("Веб-розробка", "Основи HTML, CSS та JavaScript")

        # + заняття
        python_intro = Lesson("Вступ до Python")
        python_intro.add_content(Lecture("Основи Python", "Вступ до синтаксису Python та основних концепцій"))
        python_intro.add_content(Task("Hello World", "Напишіть програму, яка виводить 'Привіт, світ!'"))

        python_advanced = Lesson("Розширений Python")
        python_advanced.add_content(Lecture("ООП в Python", "Вивчіть класи та об'єкти в Python"))
        python_advanced.add_content(Task("Створення класу", "Створіть простий клас з атрибутами та методами"))

        web_intro = Lesson("Вступ до веб-розробки")
        web_intro.add_content(Lecture("Основи HTML", "Вивчіть HTML-теги та структуру"))
        web_intro.add_content(Task("Створення веб-сторінки", "Створіть просту HTML веб-сторінку"))

        # + заняття до курсів
        python_course.add_lesson(python_intro)
        python_course.add_lesson(python_advanced)
        web_dev_course.add_lesson(web_intro)

        # + курси до менеджера
        self.add_course(python_course)
        self.add_course(web_dev_course)

        # + студенти
        student1 = Student("Іван", "Іванов", "ivan.ivanov@ukd.com", "2001-01-01")
        student2 = Student("Іванна", "Іваненко", "ivanna.ivanenko@gmail.com", "2005-05-05")

        # + студенти до менеджера
        self.add_student(student1)
        self.add_student(student2)

        # + студенти на курси
        self.enroll_student(student1.id, python_course.id)
        self.enroll_student(student2.id, python_course.id)
        self.enroll_student(student2.id, web_dev_course.id)

        # + прогрес
        student1.update_progress(python_course.id, python_intro.id, 100)
        student1.update_progress(python_course.id, python_advanced.id, 50)
        student2.update_progress(python_course.id, python_intro.id, 75)
        student2.update_progress(web_dev_course.id, web_intro.id, 30)

    # методи роботи з курсами
    def add_course(self, course):
        self.courses[course.id] = course

    def get_course_by_id(self, course_id):
        return self.courses.get(course_id)

    def get_all_courses(self):
        return list(self.courses.values())

    def create_course(self, title, description):
        course = Course(title, description)
        self.add_course(course)
        return course.id

    def update_course_title(self, course_id, new_title):
        course = self.get_course_by_id(course_id)
        if course:
            course.title = new_title

    def update_course_description(self, course_id, new_description):
        course = self.get_course_by_id(course_id)
        if course:
            course.description = new_description

    def get_course_lessons(self, course_id):
        course = self.get_course_by_id(course_id)
        if course:
            return course.lessons
        return []

    # методи роботи з заняттями
    def add_lesson(self, course_id, title):
        course = self.get_course_by_id(course_id)
        if course:
            lesson = Lesson(title)
            course.add_lesson(lesson)
            return lesson.id
        return None

    def update_lesson_title(self, course_id, lesson_id, new_title):
        course = self.get_course_by_id(course_id)
        if course:
            for lesson in course.lessons:
                if lesson.id == lesson_id:
                    lesson.title = new_title
                    return True
        return False

    def get_lesson_contents(self, course_id, lesson_id):
        course = self.get_course_by_id(course_id)
        if course:
            for lesson in course.lessons:
                if lesson.id == lesson_id:
                    return lesson.content
        return []

    # методи роботи з вмістом занять
    def add_lecture(self, course_id, lesson_id, title, content):
        course = self.get_course_by_id(course_id)
        if course:
            for lesson in course.lessons:
                if lesson.id == lesson_id:
                    lecture = Lecture(title, content)
                    lesson.add_content(lecture)
                    return lecture.id
        return None

    def add_task(self, course_id, lesson_id, title, description):
        course = self.get_course_by_id(course_id)
        if course:
            for lesson in course.lessons:
                if lesson.id == lesson_id:
                    task = Task(title, description)
                    lesson.add_content(task)
                    return task.id
        return None

    def update_lecture(self, course_id, lesson_id, content_id, new_title, new_content):
        course = self.get_course_by_id(course_id)
        if course:
            for lesson in course.lessons:
                if lesson.id == lesson_id:
                    for content in lesson.content:
                        if content.id == content_id and isinstance(content, Lecture):
                            content.title = new_title
                            content.content = new_content
                            return True
        return False

    def update_task(self, course_id, lesson_id, content_id, new_title, new_description):
        course = self.get_course_by_id(course_id)
        if course:
            for lesson in course.lessons:
                if lesson.id == lesson_id:
                    for content in lesson.content:
                        if content.id == content_id and isinstance(content, Task):
                            content.title = new_title
                            content.description = new_description
                            return True
        return False

    # методи роботи зі студентами
    def add_student(self, student):
        self.students[student.id] = student

    def get_student_by_id(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        return list(self.students.values())

    def register_student(self, first_name, last_name, email, birth_date):
        student = Student(first_name, last_name, email, birth_date)
        self.add_student(student)
        return student.id

    def enroll_student(self, student_id, course_id):
        student = self.get_student_by_id(student_id)
        course = self.get_course_by_id(course_id)

        if not student:
            return False, "Студента не знайдено."

        if not course:
            return False, "Курс не знайдено."

        # чи студент записаний на курс
        if course_id in student.get_enrolled_courses():
            return False, f"Студент вже записаний на курс '{course.title}'."

        student.enroll_in_course(course_id)
        return True, f"Студента успішно записано на курс '{course.title}'."


    def get_student_courses(self, student_id):
        student = self.get_student_by_id(student_id)
        if student:
            enrolled_courses = []
            for course_id in student.get_enrolled_courses():
                course = self.get_course_by_id(course_id)
                if course:
                    enrolled_courses.append(course)
            return enrolled_courses
        return []

    def get_student_course_progress(self, student_id, course_id):
        student = self.get_student_by_id(student_id)
        course = self.get_course_by_id(course_id)

        if not student or not course:
            return {"overall": 0, "lessons": {}}

        result = {"lessons": {}}
        total_lessons = len(course.lessons)
        completed_lessons = 0

        for lesson in course.lessons:
            progress = student.get_lesson_progress(course_id, lesson.id)
            result["lessons"][lesson.title] = progress

            if progress == 100:
                completed_lessons += 1

        result["overall"] = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
        return result

    def get_lesson_progress(self, student_id, course_id, lesson_id):
        student = self.get_student_by_id(student_id)
        if student:
            return student.get_lesson_progress(course_id, lesson_id)
        return 0

    def update_lesson_progress(self, student_id, course_id, lesson_id, progress):
        student = self.get_student_by_id(student_id)
        if student:
            student.update_progress(course_id, lesson_id, progress)
            return True
        return False

    # методи валідації
    def validate_course(self, title, description):
        return self.validators.validate_course(title, description)

    def validate_course_title(self, title):
        return self.validators.validate_course(title, "Пустий опис")

    def validate_course_description(self, description):
        return self.validators.validate_course("Пуста назва", description)

    def validate_lesson(self, title):
        return self.validators.validate_lesson(title)

    def validate_lecture(self, title, content):
        return self.validators.validate_lecture(title, content)

    def validate_task(self, title, description):
        return self.validators.validate_task(title, description)
