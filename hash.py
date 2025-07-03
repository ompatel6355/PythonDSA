my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

def hash_func(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

def add(name):
    index = hash_func(name)
    my_list[index].append(name)

def contains(name):
    index = hash_func(name)
    # return my_list[index] == name
    for i in my_list[index]:
        print(name)
        print(f'i is {i}')
        if i == name:
            print(f'match found on {index}')

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list) 
contains('Stuart')