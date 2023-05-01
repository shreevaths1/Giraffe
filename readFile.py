question_file = open("questions.txt", "r")
# question_file = open("questions.txt", "r+")
# question_file = open("questions.txt", "a")

print(question_file.readable())
# print(question_file.read())

print()
print(question_file.readline())
# print(question_file.readline())
# print(question_file.readline())
for line in question_file.readlines():
    print(line)

question_file.close()
