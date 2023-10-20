n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt_list = [0]*(n+1)

for i in range(1, m+1):
    cnt = arr.count(i)

    if cnt >= 2:
        cnt_list[cnt] += 1

dup = 0
for i in range(2, m+1):
    dup += cnt_list[i]*(i*(i-1))//2

print((n*(n-1))//2 - dup)