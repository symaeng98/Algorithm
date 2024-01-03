n = int(input())
arr = list(map(int, input().split()))
k = int(input())
cnt = 0
for a in arr:
    if a == k:
        cnt += 1

print(cnt)