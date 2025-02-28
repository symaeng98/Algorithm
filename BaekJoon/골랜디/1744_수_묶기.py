n = int(input())
plus = []
minus = []
for _ in range(n):
    x = int(input())
    if x > 0:
        plus.append(x)
    else:
        minus.append(x)

result = 0
plus.sort(reverse=True)
for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
        continue

    if plus[i] == 1 or plus[i+1] == 1:
        result += plus[i]+plus[i+1]
    else:
        result += plus[i]*plus[i+1]

minus.sort()
for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
        continue
    result += minus[i]*minus[i+1]

print(result)

# 4
# -1
# 2
# 1
# 3