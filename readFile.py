with open("questions.txt", "r") as File1:
    fileRead = File1.read()
    print(File1.readable())
    print(File1.writable())
print(fileRead)

print()
with open("questions.txt", "r") as File1:
    print(File1.read(4))
    print(File1.read(4))
    print(File1.read(4))
    print(File1.read(4))

print()
with open("questions.txt", "r") as File1:
    fileRead = File1.readlines()
print(fileRead)

print()
with open("questions.txt", "r") as File1:
    print(File1.readline(20))
    print(File1.read(20))  # reads next 20 lines

print()
with open("questions.txt", "r") as File1:
    i = 0
    for line in File1:
        print("Iteration ", i, ": ", line)
        i += 1
