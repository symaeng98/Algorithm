arr = []
for _ in range(28):
    arr.append(int(input()))

ans = []
for i in range(1, 31):
    if i not in arr:
        ans.append(i)
ans.sort()

for a in ans:
    print(a)