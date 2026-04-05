class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.student_id}, {self.name}, {self.age}, {self.grade}"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["grade"]
        )




import json
from student import Student

FILE_NAME = "students.json"

def save_students(students):
    data = [student.to_dict() for student in students]
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Student.from_dict(item) for item in data]
    except FileNotFoundError:
        return []






from student import Student
from file_manager import save_students, load_students

def add_student(students):
    student_id = input("ID: ")
    name = input("Имя: ")
    age = input("Возраст: ")
    grade = input("Оценка: ")

    student = Student(student_id, name, age, grade)
    students.append(student)
    print(" Студент добавлен")

def show_students(students):
    if not students:
        print(" Список пуст")
        return

    for student in students:
        print(student)

def delete_student(students):
    student_id = input("Введите ID для удаления: ")
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print(" Удалено")
            return
    print(" Студент не найден")

def main():
    students = load_students()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Добавить студента")
        print("2. Показать всех")
        print("3. Удалить студента")
        print("4. Сохранить")
        print("5. Выход")

        choice = input("Выберите: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            save_students(students)
            print(" Сохранено")
        elif choice == "5":
            save_students(students)
            print(" Выход")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
