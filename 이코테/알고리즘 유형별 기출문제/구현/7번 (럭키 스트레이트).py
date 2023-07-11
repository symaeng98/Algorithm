def getSum(str):
    sum = 0
    for i in range(len(str)):
        sum += int(str[i])
    return sum

strN = input()
nLength = len(strN)
leftN = strN[:nLength//2]
rightN = strN[nLength//2:]

if getSum(leftN) == getSum(rightN):
    print("LUCKY")
else:
    print("READY")