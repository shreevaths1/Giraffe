friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-2])

print()
# All elements up to but not including index 3
print(friends[1:3])
friends[1] = "Vaths"
print(friends)

print()
# List functions
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers = [42, 4, 8, 15, 16, 23]

print(friends)
friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index('Oscar'))
# print(friends.index("C"))

friends.append("Oscar")
print(friends.count("Oscar"))

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)

friends.clear()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = lucky_numbers.copy()
print(friends2)
