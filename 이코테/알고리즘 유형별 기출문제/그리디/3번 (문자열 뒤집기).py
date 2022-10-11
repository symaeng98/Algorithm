s = input()
zList = list(s.split("0"))
oList = list(s.split("1"))
zCnt = 0
oCnt = 0
for i in zList:
    if len(i) != 0:
        zCnt += 1
for j in oList:
    if len(j) != 0:
        oCnt += 1

if zCnt < oCnt:
    print(zCnt)
else:
    print(oCnt)

# split으로 길이가 0보다 큰 것의 개수만 셌는데.. 이렇게 풀면 안되나 싶었지만 어차피 O(N)인데 100만이면 괜찮지 않나 싶다