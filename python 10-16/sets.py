# myset = {"apple", "banana", "cherry"}


# myset.add("Raspberry")
# for fruit in myset:
#     print(fruit)


# print("banana" not in myset)


#Python join sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3= set1.intersection(set2)   # This we can assign value to new set
# set1.intersection_update(set2)  # This will change the original set, In this we can not assign value to new set


# set3 = set1.difference(set2)
print(set1.symmetric_difference_update(set2))
