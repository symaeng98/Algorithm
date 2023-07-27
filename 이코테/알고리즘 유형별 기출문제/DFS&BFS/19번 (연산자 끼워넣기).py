from itertools import permutations

def calculate(numList, calList):
    result = numList[0]
    index = 1
    for c in calList:
        if c == '+':
            result += numList[index]
            index += 1
        if c == '-':
            result -= numList[index]
            index += 1
        if c == '*':
            result *= numList[index]
            index += 1
        if c == '/':
            result = int(result/numList[index])
            index += 1
    return result


N = int(input())
numList = list(map(int,input().split()))
a, b, c, d = map(int,input().split())
calList = []
for i in range(a):
    calList.append("+")
for i in range(b):
    calList.append("-")
for i in range(c):
    calList.append("*")
for i in range(d):
    calList.append("/")

minResult = 10000000000
maxResult = -10000000000

for p in permutations(calList, len(calList)):
    result = calculate(numList, p)
    minResult = min(minResult, result)
    maxResult = max(maxResult, result)
print(maxResult)
print(minResult)