def sayHi(name, age):
    print("Hello " + name + " , you are " + str(age))


sayHi("Vaths", 22)
sayHi("Steve", 30)


# Return Statements
def cube(num):
    return pow(num, 3)
    # print("code")


print()
print(cube(3))
result = cube(4)
print(result)

print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")

def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a," if you add one ",b)
add(2)
# help(add)

print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")

string = "Michael Jackson is the Best"
def check_string(text):
    if text in string:
        print("String matched!")
    else:
        print("No match")
check_string("Michael Jackson")

print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")

def compare_strings(x,y):
    if x==y:
        return 1

string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"
string3 = "Elton John is the best"

check1 = compare_strings(string1,string2)
check2 = compare_strings(string1,string3)

if check1 == 1:
    print("Strings are matching")
else:
    print("String not matching.")

if check2 == 1:
    print("Strings are matching")
else:
    print("String not matching.")

print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")