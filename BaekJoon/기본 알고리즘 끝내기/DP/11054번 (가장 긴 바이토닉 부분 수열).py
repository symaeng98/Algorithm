n = int(input())
arr = list(map(int, input().split()))

dp_up = [1]*n
dp_down = [1]*n

for i in range(n):
    for j in range(i, -1, -1):
        if arr[j] < arr[i]:
            dp_up[i] = max(dp_up[i], dp_up[j]+1)

arr.reverse()
for i in range(n):
    for j in range(i, -1, -1):
        if arr[j] < arr[i]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)

dp_down.reverse()

max_value = -1
for i in range(n):
    max_value = max(max_value, dp_up[i]+dp_down[i])

print(max_value-1)