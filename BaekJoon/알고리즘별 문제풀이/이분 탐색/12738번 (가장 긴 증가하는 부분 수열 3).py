def bs(arr, x):
    if x > arr[-1]:
        return len(arr)+1
    if x < arr[0]:
        return 0

    s = 0
    e = len(arr)-1
    while s + 1 < e:
        m = (s+e)//2
        if x == arr[m]:
            return m
        elif x > arr[m]:
            s = m
        else:
            e = m

    if arr[s] == x:
        return s
    if arr[e] == x:
        return e

    return e


INF = 1e9
n = int(input())
arr = list(map(int, input().split()))
dp = [0]*n
increase_arr = [INF]*n

for i in range(len(arr)):
    index = bs(increase_arr, arr[i])
    dp[i] = index
    increase_arr[index] = arr[i]

result = 0
for a in increase_arr:
    if a == INF:
        break
    result += 1

print(result)