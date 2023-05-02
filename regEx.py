import re

s1 = "Hello! This is Vaths."
pattern1 = "\d"
pattern2 = r"Vaths"
pattern3 = "\D\D"
pattern4 = "\w\w\w\w\s"
result = re.search(pattern1, s1)
result = re.search(pattern2, s1)
result = re.search(pattern3, s1)
result = re.search(pattern4, s1)
print(result)
print()

if result:
    print("Match Found!")
else:
    print("Match not Found!")

s2 = "The cat sat on the mat"
pattern5 = "\b\w\w\w\b"
result = re.search(pattern5, s2)
print()
print(result)

s3 = "category"
pattern6 = "\Bcat\B"
result = re.search(pattern6, s3)
print()
print(result)

s2 = "The cat sat on the mat"
pattern5 = "at"
result = re.findall(pattern5, s2)
print()
print(result)

print(re.split("\s", s2))

pattern6 = "\w\w\w"
replace = "hat"
print(re.sub(pattern6, replace, s2, flags=re.IGNORECASE))
