# x = lambda a : a+ 10
# print(x(10))


#lambda in function

# def myfunc(n):
#     return lambda a: a*n

# x = myfunc(2)
# print(x(11))


# lambda with other function

numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x : x * 2, numbers))
oddNum = list(filter(lambda x: x % 2==0, numbers))
print(oddNum)