# Python has 7 types of operators
# 1. Arithmatic operation
    # This includes +, - , *, /, %, **, //



# 2. Assignment operators
    # This includes =, +=, -=, *=. /=
    # Walrus operator
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# 3. comparison operators
# 4. logical operators
    # THis include End, Or, Not


# 5. identity operators
    # This include is, is not
    
# 6. membership operators
# 7. bitwise operators