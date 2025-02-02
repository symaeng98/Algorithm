def bs(start, end, x):
    while start + 1 < end:
        mid = (start + end) // 2
        if dp[mid] == x:
            return mid
        if dp[mid] > x:
            end = mid
        else:
            start = mid

    if end == len(dp):
        return -1
    if start == -1:
        return 0
    return end


n = int(input())
arr = list(map(int, input().split()))
dp = []

for i in range(n):
    k = bs(-1, len(dp), arr[i])
    if k == -1:
        dp.append(arr[i])
    else:
        dp[k] = arr[i]
    # print(dp)
print(len(dp))
# 6
# 10 20 10 30 20 50