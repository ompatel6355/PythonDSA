my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)


#quick sort

for i in range(n):
    j = n-i
    for j in range(n-i):
        if my_array[i] > my_array[j]:
            my_array[i], my_array[j] = my_array[j], my_array[i]
            i+=1
        
print(my_array)