# def greet():
#     print("Hello! Om")

# greet()



# def my_function(name, lname):
#     print(f'Hello {name} {lname}')

# my_function("Om", "patel")


# def my_funtion():
#     return (10,20)

# x,y = my_funtion()
# print('x: ', x)
# print("y: ", y)


def my_func(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(my_func(10, 20, 30, 40))
