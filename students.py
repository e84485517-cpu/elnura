class Student:

    def __init__(self, name, age, major, gpa, courses):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.courses = courses   # словарь: курс и оценка

    def introduce(self):
        print(f"My name is {self.name}. I study {self.major}")

    def show_major(self):
        print(f"My major is {self.major}")

    def show_gpa(self):
        print(f"My gpa is {self.gpa}")

    def show_courses(self):
        print("Courses and grades:")
        for course, grade in self.courses.items():
            print(course, ":", grade)

    def add_course(self, course, grade):
        self.courses[course] = grade
        print(course, "added with grade", grade)

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        print(f"New gpa is {self.gpa}")

    def is_honor(self):
        if self.gpa > 3.5:
            print("Student is Honor")
        else:
            print("Student is not Honor")


s1 = Student("Aiza", 20, "Computer Science", 3.6, {"Python": 90, "IT": 85})

s1.introduce()

s1.show_major()

s1.show_gpa()

s1.show_courses()

s1.add_course("Algorithms", 95)

s1.show_courses()

s1.update_gpa(3.8)

s1.is_honor()
