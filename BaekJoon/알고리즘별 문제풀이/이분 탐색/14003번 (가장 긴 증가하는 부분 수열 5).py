import bisect as bi
n = int(input())
arr = list(map(int, input().split()))
dp = [0]*n
INF = 1e9

increase_arr = [INF]*n
for i, x in enumerate(arr):
    idx = bi.bisect_left(increase_arr, x)
    increase_arr[idx] = x
    dp[i] = idx

result = []
cnt = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == cnt:
        result.append(arr[i])
        cnt -= 1

print(len(result))
sorted_result = sorted(result)
for sr in sorted_result:
    print(sr, end=" ")