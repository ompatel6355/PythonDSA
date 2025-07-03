my_array = [64, 34, 25, 12, 22, 11, 90, 5]
val = 11
n = len(my_array)
for i in range(n):
    if val == my_array[i]:
        print(f'we found matching number on index {i}')

    else:
        continue
    print("No matching number")

