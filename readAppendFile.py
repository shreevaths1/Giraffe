def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as readFile:
        with open(exMem, 'a+') as writeFile:
            header = "Membership No  Date Joined  Active\n"
            readFile.readline()
            readList = readFile.readlines()


            inactList = []
            for m in readList:
                if 'no' in m:
                    inactList.append(m)

            readFile.seek(0, 0)
            # readFile.readline()
            readFile.write(header)
            for m in readList:
                if m in inactList:
                    writeFile.write(m)
                else:
                    readFile.write(m)
            readFile.truncate()


memReg = 'members1.txt'
exReg = 'inactive1.txt'
cleanFiles(memReg, exReg)

# headers = "Membership No  Date Joined  Active  \n"

with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
