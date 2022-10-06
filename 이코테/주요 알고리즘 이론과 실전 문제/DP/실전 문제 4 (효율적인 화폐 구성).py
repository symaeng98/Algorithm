N, M = map(int, input().split())
array = []
for i in range(N):
    array.append(int(input()))

numList = [0] * (M+1)
for i in range(1, M+1):
    if i - min(array) < 0:
        numList[i] = -1
        continue
    tmp = []
    for j in array:
        if i-j < 0:
            break
        if numList[i-j] == -1:
            continue
        tmp.append(numList[i-j])
    if len(tmp) == 0:
        numList[i] = -1
        continue
    numList[i] = min(tmp) + 1

print(numList[M])