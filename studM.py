class Student:  
    def __init__(self, name, student_id, grades):  
        self.name = name  
        self.student_id = student_id  
        self.grades = grades  

    def add_grade(self, grade): 
        self.grades.append(grade) 

    def calculate_average(self):  
        return sum(self.grades) / len(self.grades)  

    def get_best_grade(self): 
        return max(self.grades)  

    def get_worst_grade(self):  
        return min(self.grades)  

    def display_info(self):  
        print("Имя:", self.name)  
        print("ID:", self.student_id)  
        print("Оценки:", self.grades)  
        print("Средний балл:", round(self.calculate_average(), 2))  
        print("Лучшая оценка:", self.get_best_grade())  
        print("Худшая оценка:", self.get_worst_grade())  
        print("-" * 20)  


class StudentManager:
    def __init__(self):  
        self.students = []  

    def add_student(self, student):  
        self.students.append(student)  

    def display_all_students(self):  
        for student in self.students:  
            student.display_info() 

    def get_top_student(self):  
        top_student = self.students[0]  
        for student in self.students:  
            if student.calculate_average() > top_student.calculate_average():  
                top_student = student  
        return top_student  

    def get_lowest_student(self):  
        low_student = self.students[0]  
        for student in self.students:  
            if student.calculate_average() < low_student.calculate_average():  
                low_student = student  
        return low_student  

manager = StudentManager()  

student1 = Student("Эльнура", 101, [70, 75, 80])  
student2 = Student("Аиза", 102, [90, 95, 100])  

manager.add_student(student1)  
manager.add_student(student2) 

print("Все студенты:")  
manager.display_all_students()  


print("Лучший студент:")  
top_student = manager.get_top_student()  
top_student.display_info()  


print("Студент с худшими оценками:")  
worst_student = manager.get_lowest_student()  
worst_student.display_info()  
