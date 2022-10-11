n = int(input())
arr = list(map(int,input().split()))
arr.sort()

cnt = 0
group = 0
for a in arr:
    group += 1
    if group >= a:
        cnt += 1
        group = 0

print(cnt)