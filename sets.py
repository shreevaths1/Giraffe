s = {1,2,3,4,5}
s.add(2.5)
print('s.add(2.5): ', )
s.add(2)
print('s.add(2): ', s)
print('s.clear: ', s.clear())

s = {1,2,3,4,5}
sc = s.copy()
print('sc = s.copy(): ', sc)

print("--- --- --- --- --- --- ---")
s1 = {1,2,3,4}
s2 = {4,5,6,7}


print('s1.intersection(s2): ', s1.intersection(s2))

print('s1.difference(s2): ', s1.difference(s2))

print('s1.union(s2): ', s1.union(s2))

print('s1.isdisjoint(s2): ', s1.isdisjoint(s2))

s2.difference_update(s1)
print('s2.difference_update(s1): ', s2)

s2.intersection_update(s1)
print('s2.intersection_update(s1): ', s2)

s2 = {4,5,6,7}
print('s2.remove(5): ', s2.remove(5))
print("--- --- --- --- --- --- ---")

s3 = {1,2,3,4}
s4 = {3,4}

print('s4.issubset(s3): ', s4.issubset(s3))

print('s3.issubset(s4): ', s3.issubset(s4))

print('s3.issuperset(s4): ', s3.issuperset(s4))

print('s4.issuperset(s3): ', s4.issuperset(s3))


print('s1.symmetric_difference(s2): ', s1.symmetric_difference(s2))

s1.symmetric_difference_update(s2)
print('s1.symmetric_difference_update(s2): ', s1)

print('s1.pop(): ', s1.pop())
s1.discard(7)
print('s1.discard(7): ', s1)

s2.update([9,10])
print('s2.update([9,10]): ', s2)