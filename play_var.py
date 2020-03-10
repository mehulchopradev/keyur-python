a = 10 # entire module
b = 34 # entire module
c = 10 # entire module
d = 54 # entire module

def fun():
    # getting the value of the variable a
    print(a) # 10

    b = 45 # fun()
    print(b) # 45

    ''' c = c + 45 # this will not work
    print(c) '''

    global d
    d = d + 10 # u r modifying the global variable (avoid it!!)
    print(d)


fun()
print(b) # 34
print(c)
print(d) # 64