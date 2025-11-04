# A variable is only available from inside the region it it created. This is called scope
x = 300 #global keyword, can be used anywhere in code
def my_funct():
    #we can also modify global scope here 
    x = 500 #inner scope, Only can be used inside the function or function inside function
    def my_innerFunc():
        print(x)
    my_innerFunc()

my_funct()
    