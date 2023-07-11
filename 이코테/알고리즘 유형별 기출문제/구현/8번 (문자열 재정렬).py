# S = input()
# sList = []
# for i in range(len(S)):
#     sList.append(S[i])
#
# sList.sort()
#
# strStartIndex = -1
# for idx, value in enumerate(sList):
#     if not ("0" <= value <= "9"):
#         strStartIndex = idx
#         break
#
# numList = sList[:strStartIndex]
# sum = 0
# for n in numList:
#     sum += int(n)
#
# if sum == 0:
#     for s in sList[strStartIndex:]:
#         print(s,end="")
# else:
#     for s in sList[strStartIndex:]:
#         print(s,end="")
#     print(str(sum))


## 답
S = input()
result = []
sum = 0

for s in S:
    if s.isalpha():
        result.append(s)
    else:
        sum += int(s)

result.sort()

if sum != 0:
    result.append(str(sum))

print(''.join(result))
