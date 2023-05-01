from Student import Student

student1 = Student("Jim", "Computer Science", 9.82, False)
student2 = Student("Pam", "Arts", 9.54, True)

print(student1.name)
print(student1.major)
print(student1.gpa > student2.gpa)

print()
print(student1.isOnHonorRoll())
print(student2.isOnHonorRoll())
