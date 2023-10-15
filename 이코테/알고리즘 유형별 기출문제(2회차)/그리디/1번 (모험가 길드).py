n = int(input())
arr = list(map(int, input()))

arr.sort()
group = 0
cnt = 0
for a in arr:
    group += 1
    if a <= group:
        cnt += 1
        group = 0
print(cnt)