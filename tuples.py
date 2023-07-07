# useful for denoting corrdinates
coordinates = (4, 5)
# tuples not mutable
# coordinates[1] = 10
print(coordinates[1])

print("--- --- --- --- --- --- ---")
# Tuple methods
tuple1 = (1,2.5,0.5,0.5)
print("count 0.5 in tuple1 : ",tuple1.count(0.5))
print("index of 2.5 in tuple1 : ",tuple1.index(2.5))
print("sorted tuple1 : ",sorted(tuple1))


print("--- --- --- --- --- --- ---")
# Nested tuple
NT = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))
print("NT : ",NT)
print("NT[4][1][1] : ",NT[4][1][1])
print("NT.index((\"pop\", \"rock\")) : ",NT.index(("pop", "rock")))
