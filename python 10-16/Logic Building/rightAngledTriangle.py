# n = int(input("Enter number of rows: "))
n = 5

for i in range(1, n):
    s = ""
    for j in range(1, i):
        s += "*"

    print(s)