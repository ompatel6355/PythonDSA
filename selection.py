my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n):
    min_index = 0
    for j in range(i, n-1):
        if my_array[j] < my_array[min_index]:
            min_index = j
    # Swap the found minimum element with the first element
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print(my_array)
