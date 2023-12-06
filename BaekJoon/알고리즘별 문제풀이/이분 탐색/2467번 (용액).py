n = int(input())
arr = list(map(int, input().split()))

arr.sort()

start = 0
end = n-1
min_zero_value = abs(arr[start] + arr[end])
result = [arr[start], arr[end]]

while start < end:
    s_value = arr[start]
    e_value = arr[end]
    sum_value = s_value + e_value

    if min_zero_value > abs(sum_value):
        min_zero_value = abs(sum_value)
        result[0] = s_value
        result[1] = e_value

    if sum_value < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])