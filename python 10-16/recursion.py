# def countdown(n):
#     if n <= 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n-1)



# def fact(n):
#     if n==0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
        
# x = fact(5)
# print(x)


import sys
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
x = fib(7)
print(sys.getrecursionlimit())