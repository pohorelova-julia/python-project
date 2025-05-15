from course_manager import CourseManager

def display_menu():
    print("""
    ----- СИСТЕМА ОНЛАЙН-КУРСІВ -----
    1. Створити новий курс
    2. Додати заняття до курсу
    3. Редагувати курс
    4. Зареєструвати нового студента
    5. Записати студента на курс
    6. Переглянути прогрес студента
    7. Переглянути всі курси
    8. Переглянути всіх студентів
    9. Оновити прогрес студента
    10. Вихід
    """)


def create_course_action(course_manager):
    print("\n----- Створення нового курсу -----")

    while True:
        title = input("Введіть назву курсу: ")
        description = input("Введіть опис курсу: ")

        valid, message = course_manager.validate_course(title, description)
        if not valid:
            print(f"Помилка: {message} Спробуйте ще раз.")
            continue

        course_manager.create_course(title, description)
        print(f"Курс '{title}' успішно створено.")
        break


def add_lesson_to_course_action(course_manager):
    print("\n----- Додавання заняття до курсу -----")
    view_all_courses_action(course_manager)

    course_id = input("Введіть ID курсу: ")
    course = course_manager.get_course_by_id(course_id)

    if not course:
        print("Курс не знайдено.")
        return

    while True:
        title = input("Введіть назву заняття: ")

        valid, message = course_manager.validate_lesson(title)
        if not valid:
            print(f"Помилка: {message} Спробуйте ще раз.")
            continue

        lesson_id = course_manager.add_lesson(course_id, title)
        print(f"Заняття '{title}' створено з ID: {lesson_id}")
        break

    while True:
        print("""
        Додати вміст до заняття:
        1. Додати лекцію
        2. Додати завдання
        3. Завершити додавання вмісту
        """)

        content_choice = input("Введіть ваш вибір (1-3): ")

        if content_choice == "1":
            while True:
                lecture_title = input("Введіть назву лекції: ")
                lecture_content = input("Введіть вміст лекції: ")

                valid, message = course_manager.validate_lecture(lecture_title, lecture_content)
                if not valid:
                    print(f"Помилка: {message} Спробуйте ще раз.")
                    continue

                course_manager.add_lecture(course_id, lesson_id, lecture_title, lecture_content)
                print("Лекцію успішно додано.")
                break

        elif content_choice == "2":
            while True:
                task_title = input("Введіть назву завдання: ")
                task_description = input("Введіть опис завдання: ")

                valid, message = course_manager.validate_task(task_title, task_description)
                if not valid:
                    print(f"Помилка: {message} Спробуйте ще раз.")
                    continue

                course_manager.add_task(course_id, lesson_id, task_title, task_description)
                print("Завдання успішно додано.")
                break

        elif content_choice == "3":
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


def edit_course_action(course_manager):
    print("\n----- Редагування курсу -----")
    view_all_courses_action(course_manager)

    course_id = input("Введіть ID курсу для редагування: ")
    course = course_manager.get_course_by_id(course_id)

    if not course:
        print("Курс не знайдено.")
        return

    print(f"""
    Редагування курсу: {course.title}
    1. Редагувати назву
    2. Редагувати опис
    3. Редагувати заняття
    """)

    edit_choice = input("Введіть ваш вибір (1-3): ")

    if edit_choice == "1":
        while True:
            new_title = input("Введіть нову назву: ")

            valid, message = course_manager.validate_course_title(new_title)
            if not valid:
                print(f"Помилка: {message} Спробуйте ще раз.")
                continue

            course_manager.update_course_title(course_id, new_title)
            print("Назву успішно оновлено.")
            break

    elif edit_choice == "2":
        while True:
            new_description = input("Введіть новий опис: ")

            valid, message = course_manager.validate_course_description(new_description)
            if not valid:
                print(f"Помилка: {message} Спробуйте ще раз.")
                continue

            course_manager.update_course_description(course_id, new_description)
            print("Опис успішно оновлено.")
            break

    elif edit_choice == "3":
        lessons = course_manager.get_course_lessons(course_id)
        print("\nПоточні заняття:")
        for i, lesson in enumerate(lessons):
            print(f"{i + 1}. {lesson.title} (ID: {lesson.id})")

        lesson_idx = int(input("Введіть номер заняття для редагування (або 0 для повернення): ")) - 1

        if 0 <= lesson_idx < len(lessons):
            lesson = lessons[lesson_idx]

            print(f"""
            Редагування заняття: {lesson.title}
            1. Редагувати назву
            2. Редагувати вміст
            """)

            lesson_edit_choice = input("Введіть ваш вибір (1-2): ")

            if lesson_edit_choice == "1":
                while True:
                    new_title = input("Введіть нову назву: ")

                    valid, message = course_manager.validate_lesson(new_title)
                    if not valid:
                        print(f"Помилка: {message} Спробуйте ще раз.")
                        continue

                    course_manager.update_lesson_title(course_id, lesson.id, new_title)
                    print("Назву заняття успішно оновлено.")
                    break

            elif lesson_edit_choice == "2":
                contents = course_manager.get_lesson_contents(course_id, lesson.id)
                print("\nПоточний вміст:")
                for i, content in enumerate(contents):
                    content_type = content.get_type()
                    print(f"{i + 1}. [{content_type}] {content.title}")

                content_idx = int(input("Введіть номер вмісту для редагування (або 0 для повернення): ")) - 1

                if 0 <= content_idx < len(contents):
                    content = contents[content_idx]
                    content_type = content.get_type()

                    print(f"\nРедагування {content_type}: {content.title}")

                    if content_type == "Лекція":
                        while True:
                            new_title = input("Введіть нову назву: ")
                            new_content = input("Введіть новий вміст лекції: ")

                            valid, message = course_manager.validate_lecture(new_title, new_content)
                            if not valid:
                                print(f"Помилка: {message} Спробуйте ще раз.")
                                continue

                            course_manager.update_lecture(course_id, lesson.id, content.id, new_title, new_content)
                            print("Лекцію успішно оновлено.")
                            break
                    else:
                        while True:
                            new_title = input("Введіть нову назву: ")
                            new_description = input("Введіть новий опис завдання: ")

                            valid, message = course_manager.validate_task(new_title, new_description)
                            if not valid:
                                print(f"Помилка: {message} Спробуйте ще раз.")
                                continue

                            course_manager.update_task(course_id, lesson.id, content.id, new_title, new_description)
                            print("Завдання успішно оновлено.")
                            break
    else:
        print("Невірний вибір.")


def register_student_action(course_manager):
    print("\n----- Реєстрація нового студента -----")
    first_name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")
    email = input("Введіть email: ")
    birth_date = input("Введіть дату народження (РРРР-ММ-ДД): ")

    student_id = course_manager.register_student(first_name, last_name, email, birth_date)
    print(f"Студента успішно зареєстровано з ID: {student_id}")


def enroll_student_action(course_manager):
    print("\n----- Запис студента на курс -----")
    view_all_students_action(course_manager)
    student_id = input("Введіть ID студента: ")

    student = course_manager.get_student_by_id(student_id)
    if not student:
        print("Студента не знайдено.")
        return

    view_all_courses_action(course_manager)
    course_id = input("Введіть ID курсу: ")

    # перевірка на наявність студента в курсі
    success, message = course_manager.enroll_student(student_id, course_id)
    print(message)


def view_student_progress_action(course_manager):
    print("\n----- Перегляд прогресу студента -----")
    view_all_students_action(course_manager)
    student_id = input("Введіть ID студента: ")

    student = course_manager.get_student_by_id(student_id)
    if not student:
        print("Студента не знайдено.")
        return

    print(f"\nПрогрес для {student.first_name} {student.last_name}:")

    enrolled_courses = course_manager.get_student_courses(student_id)
    if not enrolled_courses:
        print("Студент не записаний на жодний курс.")
        return

    for course in enrolled_courses:
        print(f"\nКурс: {course.title}")

        progress_data = course_manager.get_student_course_progress(student_id, course.id)

        print("\nПрогрес по заняттях:")
        for lesson_title, progress in progress_data["lessons"].items():
            print(f"  - {lesson_title}: {progress}% виконано")

        print(f"Загальний прогрес по курсу: {progress_data['overall']:.1f}%")


def update_student_progress_action(course_manager):
    print("\n----- Оновлення прогресу студента -----")
    view_all_students_action(course_manager)
    student_id = input("Введіть ID студента: ")

    student = course_manager.get_student_by_id(student_id)
    if not student:
        print("Студента не знайдено.")
        return

    enrolled_courses = course_manager.get_student_courses(student_id)
    if not enrolled_courses:
        print("Студент не записаний на жодний курс.")
        return

    print("\nКурси, на які записаний студент:")
    for i, course in enumerate(enrolled_courses):
        print(f"{i + 1}. {course.title} (ID: {course.id})")

    course_idx = int(input("Виберіть номер курсу: ")) - 1

    if 0 <= course_idx < len(enrolled_courses):
        course = enrolled_courses[course_idx]

        lessons = course_manager.get_course_lessons(course.id)
        print(f"\nЗаняття в курсі '{course.title}':")
        for i, lesson in enumerate(lessons):
            current_progress = course_manager.get_lesson_progress(student_id, course.id, lesson.id)
            print(f"{i + 1}. {lesson.title} (Поточний прогрес: {current_progress}%)")

        lesson_idx = int(input("Виберіть номер заняття: ")) - 1

        if 0 <= lesson_idx < len(lessons):
            lesson = lessons[lesson_idx]
            new_progress = int(input(f"Введіть новий прогрес для заняття '{lesson.title}' (0-100): "))

            if 0 <= new_progress <= 100:
                course_manager.update_lesson_progress(student_id, course.id, lesson.id, new_progress)
                print(f"Прогрес успішно оновлено до {new_progress}%.")
            else:
                print("Прогрес повинен бути в межах від 0 до 100.")
        else:
            print("Невірний номер заняття.")
    else:
        print("Невірний номер курсу.")

def view_all_courses_action(course_manager):
    print("\n---- Всі курси ----")
    courses = course_manager.get_all_courses()

    if not courses:
        print("Немає доступних курсів.")
        return

    for course in courses:
        print(f"\n--- Курс: {course.title} (ID: {course.id}) ---")
        print(f"Опис: {course.description}")

        if not course.lessons:
            print("Курс не містить занять.")
            continue

        print("\nЗаняття:")
        for i, lesson in enumerate(course.lessons):
            print(f"\n  {i + 1}. {lesson.title} (ID: {lesson.id})")

            if not lesson.content:
                print("    Заняття не містить вмісту.")
                continue

            print("    Вміст:")
            for j, content in enumerate(lesson.content):
                if hasattr(content, 'content'):
                    print(f"      {j + 1}. Лекція. {content.title}")
                    print(f"         Вміст: {content.content}")
                else:
                    print(f"      {j + 1}. Завдання. {content.title}")
                    print(f"         Опис: {content.description}")


def view_all_students_action(course_manager):
    print("\n----- Всі студенти -----")
    students = course_manager.get_all_students()

    if not students:
        print("Немає зареєстрованих студентів.")
        return

    for student in students:
        print(f"ID: {student.id} | Ім'я: {student.first_name} {student.last_name} | Email: {student.email}")


def main():
    course_manager = CourseManager()

    # + дані для прикладу
    course_manager.load_sample_data()

    while True:
        display_menu()
        choice = input("Введіть ваш вибір (1-10): ")

        if choice == "1":
            create_course_action(course_manager)
        elif choice == "2":
            add_lesson_to_course_action(course_manager)
        elif choice == "3":
            edit_course_action(course_manager)
        elif choice == "4":
            register_student_action(course_manager)
        elif choice == "5":
            enroll_student_action(course_manager)
        elif choice == "6":
            view_student_progress_action(course_manager)
        elif choice == "7":
            view_all_courses_action(course_manager)
        elif choice == "8":
            view_all_students_action(course_manager)
        elif choice == "9":
            update_student_progress_action(course_manager)
        elif choice == "10":
            print("Дякуємо за використання Системи Онлайн-Курсів. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
