'''
question_file=open("questions.txt","a")
question_file.write("\nGood Bye!")
question_file.close()


question_file=open("questions.txt", "w")
question_file.write("Good Bye!")
question_file.close()

'''

with open("questions.txt", "w+") as File2:
    File2.write("This is line 1\n")
    print(File2.tell())
    File2.seek(0, 0)
    print(File2.tell())
    print(File2.read())
    print(File2.tell())

with open("questions.txt","a") as File2:
    File2.write("hello")
