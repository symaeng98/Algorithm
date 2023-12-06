n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = n - 1

answer = abs(arr[start] + arr[end])
result = [arr[start], arr[end]]
while start < end:
    start_val = arr[start]
    right_val = arr[end]

    sum_value = start_val + right_val

    if abs(sum_value) < answer:
        answer = abs(sum_value)
        result = [start_val, right_val]
        if answer == 0:
            break
    if sum_value < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])