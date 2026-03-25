код который я писала в универе:
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, age, salary):
         self.name = name
         self.age = age
         self.salary = salary

     @abstractmethod
     def work(self):
         pass

     def display_info(self):
         print(f"Имя: {self.name}, Возраст: {self.age}, Зарплата: {self.salary}")

 class Developer(Employee):
     def __init__(self, name, age, salary, programming_language):
         super().__init__(name, age, salary)
         self.programming_language = programming_language

     def work(self):
         print(f"{self.name} пишет код на {self.programming_language}.")
class Manager(Employee):
     def __init__(self, name, age, salary, team_size):
         super().__init__(name, age, salary)
         self.team_size = team_size

     def work(self):
         print(f"{self.name} управляет командой из {self.team_size} сотрудников.")

 dev = Developer("Алекс", 30, 70000, "Python")
 mgn = Manager("Екатерина", 35, 90000, 10)

 dev.display_info()
 dev.work()
 mgn.display_info()
 mgn.work()



#переделала
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

class Developer(Employee):
    def work(self):
        return "Алекс пишет код на Python."

    def display_info(self):
        return "Имя: Алекс, Возраст: 30, Зарплата: 70000"

class Manager(Employee):
    def work(self):
        return "Екатерина управляет командой из 10 сотрудников."

    def display_info(self):
        return "Имя: Екатерина, Возраст: 35, Зарплата: 90000"

def sound(employee):
    print(employee.work())

def look(employee):
    print(employee.display_info())

sound(Developer())
sound(Manager())

look(Developer())
look(Manager())




