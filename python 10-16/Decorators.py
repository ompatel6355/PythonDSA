# def change_case(funct):
#     def myinner(*x):
#         return funct(*x).upper()
#     return myinner

# @change_case
# def myfunct(name, lname):
#     return f'Hello {name} or mr.{lname}'
    
# print(myfunct("Om", "Patel"))



# Both *args and **kwargs example
# def changecase(funct):
#     def myinnner(*args, **kwargs):
#         return funct(*args, **kwargs).upper()
#     return myinnner

# @changecase
# def myfunc(name):
#     return "hello " + name

# print(myfunc("Om"))



#Decorators with arguments


# def changeCase(n):
#     def changeCase(func):
#         def myinner():
#             if n == 1:
#                 a = func().lower()

#             else:
#                 a = func().upper()
#             return a
#         return myinner
#     return changeCase

# @changeCase(1)
# def myfunct():
#     return "Hello Om"

# print(myfunct())



# multiple Decorators
import functools

def changeCase(funct):
    @functools.wraps(funct)

    def myinner():
        return funct().upper()
    return myinner

def greetings(funct):
    @functools.wraps(funct)
    def myinner():
        return f'Hello {funct()}'
    return myinner

@changeCase
@greetings
def myfunc():
    return "Om"

print(myfunc.__name__)