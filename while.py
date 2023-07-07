i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with while loop.")

print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")

squares = ['orange', 'orange', 'purple', 'blue', 'orange']
new_squares = []
i = 0
s = squares[0]
while s == 'orange' and i < len(squares):
    new_squares.append(s)
    i += 1
    if i < len(squares):
        s = squares[i]
print(new_squares)