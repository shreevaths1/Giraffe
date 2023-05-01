# global variable
x = 101


def mainFunction():

    global x
    print(x)

    x = "Welcome to Python"
    print(x)

    # local variable
    y = 20
    print(y)


mainFunction()
print("Outside Function...")
print(x)
# print(y)
