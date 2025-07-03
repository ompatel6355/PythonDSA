my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n):
    for j in range(0, n-i-1):
        if my_array[j] > my_array[j+1]:
            # Swap if the element found is greater
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print(my_array)