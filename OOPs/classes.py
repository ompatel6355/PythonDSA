# class person:
#     x = "OM"

# p1 = person()
# print(person.x)


# class person:   
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def greetings(self):
#         print(f'hello {self.fname} and your last name is {self.lname}')
    

# x = person("om", "patel")

# x.greetings()


class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f'Hello'
    def welcome(self):
        message = self.greet()
        return f'{message}! Welcome to the hood {self.name}'

p1 = Person("Om")
print(p1.welcome())
# print(p1.greet())
