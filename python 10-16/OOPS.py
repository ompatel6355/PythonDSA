# Class is a blueprint for creating object

# class Student:
#     name = "Om"
# s1 = Student()
# print(s1.name)



# Constructor class or __INIT__ function

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def hello(self):
        print("You're at the top,", self.name)

s1 = Student("Om", 99)
print(s1.name, s1.grade)
s1.hello()