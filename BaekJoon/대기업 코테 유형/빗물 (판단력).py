h, w = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(1, w-1):
    left = max(arr[:i])
    right = max(arr[i+1:])

    min_h = min(left, right)

    if arr[i] < min_h:
        result += min_h - arr[i]

print(result)