def change_case(funct):
    def myinner(*x):
        return funct(*x).upper()
    return myinner

@change_case
def myfunct(name, lname):
    return f'Hello {name} or mr.{lname}'
    
print(myfunct("Om", "Patel"))