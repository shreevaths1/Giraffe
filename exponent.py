def raiseToPow(baseNum, powNum):
    result = 1
    for i in range(powNum):
        result = result * baseNum
    return result


print(raiseToPow(2, 10))
