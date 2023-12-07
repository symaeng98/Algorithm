n = int(input())
arr = list(map(int, input().split()))
dp = [1]
max_cnt = 1

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            if max_cnt <= dp[j]:
                max_cnt = dp[j] + 1
        else:
            continue
    dp.append(max_cnt)
    max_cnt = 1

print(max(dp))