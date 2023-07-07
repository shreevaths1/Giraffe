try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    # print("Division by zero")
    print(err)
except ValueError:
    print("Invalid Input")

print("--- --- --- --- --- --- --- --- --- ---")

try:
    num = int(input("Enter a number : "))
    a = 35 / num
    print(f"35 / {num} = ",a)
except:
    print("Invalid Input!")

print("--- --- --- --- --- --- --- --- --- ---")

a = 1
try:
    b = int(input("Enter a number to divide by 'a' : "))
    a = a / b
    print(f"result = {a}")
except ZeroDivisionError:
    print("you can't divide a number by zero.")
except ValueError:
    print("No value provided.")
except:
    print("Unknown error occured!")

print("--- --- --- --- --- --- --- --- --- ---")

a = 1
try:
    b = int(input("Enter a number to divide by 'a' : "))
    a = a / b
    
except ZeroDivisionError:
    print("you can't divide a number by zero.")
except ValueError:
    print("No value or invalid input provided.")
except:
    print("Unknown error occured!")
else:
    print(f"result = {a}")
finally:
    # print(a)
    print("Process terminated sucessfully.")

print("--- --- --- --- --- --- --- --- --- ---")