class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def median(self):
        op = (self.mark1 + self.mark2 + self.mark3) / 3
        print(self.name, " average marks is", op)

s1 = Student("om", 95, 98, 88)
s1.median()
