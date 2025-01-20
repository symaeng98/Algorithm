n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = [arr[0], arr[n-1]]
now = abs(arr[0] + arr[n-1])
left, right = 0, n - 1

while left < right:
    sum_value = arr[left]+arr[right]
    if abs(sum_value) < now:
        now = abs(sum_value)
        result[0] = arr[left]
        result[1] = arr[right]

    if abs(sum_value) == 0:
        break

    if sum_value < 0:
        left += 1
    else:
        right -= 1


print(*result)

# 5
# -2 4 -99 -1 98