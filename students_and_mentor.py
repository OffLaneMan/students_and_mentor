class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if 0 <= grade <= 10:
            if (
                isinstance(lecturer, Lector)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached
            ):
                if course in lecturer.Lecturer:
                    lecturer.Lecturer[course] += [grade]
                else:
                    lecturer.Lecturer[course] = [grade]
        else:
            return "Оценка должна быть от 0 до 10"

    def __str__(self):
        grades = [y for x in self.grades.values() for y in x]
        average_grade = (
            f"{sum(grades) / len(grades):.1f}" if len(grades) > 0 else "Оценок нет"
        )
        courses_in_progress = (
            ", ".join(self.courses_in_progress)
            if len(self.courses_in_progress) > 0
            else "Не изучает ни одного курса"
        )
        finished_courses = (
            ", ".join(self.finished_courses)
            if len(self.finished_courses) > 0
            else "Ничего не завершено"
        )
        courses_in_progress = ", ".join(self.courses_in_progress)
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Cредняя оценка за домашние задания: {average_grade}
Курсы в процессе изучения: {courses_in_progress}
Завершенные курсы: {finished_courses}"""


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.Lecturer = {}

    def __str__(self):
        grades = [y for x in self.Lecturer.values() for y in x]
        average_grade = (
            f"{sum(grades) / len(grades):.1f}" if len(grades) > 0 else "Оценок нет"
        )
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {average_grade}"""


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if 0 <= grade <= 10:
            if (
                isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress
            ):
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return "Ошибка"
        else:
            return "Оценка должна быть от 0 до 10"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


student1 = Student("Piter", "Parker", "male")
student2 = Student("Mari", "Jane", "gender")
reviewers1 = Reviewer("Ivan", "Ivanov")
reviewers2 = Reviewer("Andrey", "Andreev")
lectors1 = Lector("Ilone", "Mask")
lectors2 = Lector("Denis", "Denisov")

student1.finished_courses = ["javascript"]

student1.courses_in_progress = ["python"]
student2.courses_in_progress = ["python"]

reviewers1.courses_attached = ["python"]
reviewers2.courses_attached = ["javascript"]

lectors1.courses_attached = ["python"]
lectors2.courses_attached = ["javascript"]

reviewers1.rate_hw(student1, "python", 10)
reviewers1.rate_hw(student1, "python", 9)
reviewers1.rate_hw(student1, "python", 7)
reviewers2.rate_hw(student1, "python", 10)
reviewers2.rate_hw(student1, "python", 9)
reviewers2.rate_hw(student1, "python", 7)
reviewers1.rate_hw(student2, "python", 10)
reviewers1.rate_hw(student2, "python", 8)
reviewers1.rate_hw(student2, "python", 7)
reviewers2.rate_hw(student2, "python", 10)
reviewers2.rate_hw(student2, "python", 8)
reviewers2.rate_hw(student2, "python", 7)

student1.rate_lecturer(lectors1, "python", 10)
student1.rate_lecturer(lectors2, "python", 9)


# print(student1)
# print(student2)
# print(lectors1)
# print(lectors2)
# print(reviewers1)
# print(reviewers2)


def average_rate_students(students, course):
    grades = []
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                grades += value
    return f"Средняя оценка за домашние задания по всем студентам: {sum(grades) / len(grades):.1f}"


def average_rate_lectors(lectors, course):
    grades = []
    for lector in lectors:
        for key, value in lector.Lecturer.items():
            if key == course:
                grades += value
    return f"Средняя оценка за лекции по всем лекторам: {sum(grades) / len(grades):.1f}"


# print(average_rate_students([student1, student2], "python"))
# print(average_rate_lectors([lectors1, lectors2], "python"))
