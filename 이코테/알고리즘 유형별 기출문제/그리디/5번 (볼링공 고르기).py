n, m = map(int, input().split(" "))
arr = list(map(int, input().split()))
cntList = [0] * m
for a in arr:
    cntList[a-1] += 1

result = (n * (n - 1)) // 2
exception = 0
for c in cntList:
    if c <= 1:
        continue
    exception += (c * (c-1)) // 2

result -= exception
print(result)