# If Statements
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both.")
    print()
else:
    print("You are neither male nor tall.")
print("--- --- --- --- --- --- --- --- --- ---")

is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male.")
else:
    print("You are either not male or not tall or not both")

print("--- --- --- --- --- --- --- --- --- ---")
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are not a male but are tall.")
else:
    print("You are neither a male nor tall.")
print("--- --- --- --- --- --- --- --- --- ---")
