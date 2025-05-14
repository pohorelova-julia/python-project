class Validators:
    @staticmethod
    def validate_course(title, description):
        if not title or title.strip() == "":
            return False, "Назва курсу не може бути порожньою."

        if not description or description.strip() == "":
            return False, "Опис курсу не може бути порожнім."

        if len(title) < 3:
            return False, "Назва курсу повинна містити щонайменше 3 символи."

        if len(description) < 10:
            return False, "Опис курсу повинен містити щонайменше 10 символів."

        return True, None

    @staticmethod
    def validate_lesson(title):
        if not title or title.strip() == "":
            return False, "Назва заняття не може бути порожньою."

        if len(title) < 3:
            return False, "Назва заняття повинна містити щонайменше 3 символи."

        return True, None

    @staticmethod
    def validate_lecture(title, content):
        if not title or title.strip() == "":
            return False, "Назва лекції не може бути порожньою."

        if not content or content.strip() == "":
            return False, "Вміст лекції не може бути порожнім."

        if len(title) < 3:
            return False, "Назва лекції повинна містити щонайменше 3 символи."

        if len(content) < 10:
            return False, "Вміст лекції повинен містити щонайменше 10 символів."

        return True, None

    @staticmethod
    def validate_task(title, description):
        if not title or title.strip() == "":
            return False, "Назва завдання не може бути порожньою."

        if not description or description.strip() == "":
            return False, "Опис завдання не може бути порожнім."

        if len(title) < 3:
            return False, "Назва завдання повинна містити щонайменше 3 символи."

        if len(description) < 10:
            return False, "Опис завдання повинен містити щонайменше 10 символів."

        return True, None