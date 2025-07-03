my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n):
    key = my_array[i]
    j = i - 1
    while j >=0 and key < my_array[j]:
        my_array[j+1] = my_array[j]
        j-= 1
    my_array[j+1] = key


print(my_array)