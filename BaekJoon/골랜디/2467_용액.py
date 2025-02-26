n = int(input())
arr = list(map(int, input().split()))

left, right = 0, len(arr)-1

result = [arr[left], arr[right]]
min_result = abs(arr[left] + arr[right])
while left < right:
    sum_value = arr[left] + arr[right]
    if min_result > abs(sum_value):
        min_result = abs(sum_value)
        result = [arr[left], arr[right]]

    if sum_value < 0:
        left += 1
    else:
        right -= 1

result.sort()
print(*result)
