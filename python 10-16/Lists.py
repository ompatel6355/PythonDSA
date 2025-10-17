my_arr = [7,12,9,4]
minVal = my_arr[0]
for val in my_arr:
    if val < minVal:
        minVal = val

print("Lowest integer in list is, ", minVal)