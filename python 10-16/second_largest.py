my_arr2 = [7,12,9,4, 1, 15, 99, 250, 50]
curr_max = my_arr2[0]
arr_max = []

for i in range(len(my_arr2)):
    if my_arr2[i] < curr_max:
        continue
    else:
        curr_max = my_arr2[i]
        arr_max.append(my_arr2[i])

print(arr_max[-2])