friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-2])

print("--- --- --- --- --- --- ---")
# All elements up to but not including index 3
print(friends[1:3])
# lists are mutable. changing element at index 1
friends[1] = "Vaths"
print(friends)


print('len(friends): ', len(friends))

print('sum([1,2,3,4,5,6,7,8,9,10]): ', sum([1,2,3,4,5,6,7,8,9,10]))

print("--- --- --- --- --- --- ---")
# List functions
list1 = [1,2.5,0.5,0.5]

print("print append operation : ",list1.append(2))
print("append 2 to list1 : ",list1)

list1.clear()

list2 = list1.copy()
list2.append(4)
print("list1 : ",list1)
print("list2 : ",list2)

print("count 0.5 in list1 : ",list1.count(0.5))

list1.extend([4])
print("extend list1 : ",list1)

print("index of 4 in list1 : ",list1.index(4))

list1.insert(2,'buddy')
print("after inserting 'buddy' : ",list1)

print("popping : ",list1.pop())
print("after popping : ",list1)

list1.remove(4)
print("remove 4 from list1 : ",list1)

list1 = [1,2.5,0.5,0.5]
print("before reversing list1 : ",list1)
list1.reverse()
print("after reversing list1 : ",list1)