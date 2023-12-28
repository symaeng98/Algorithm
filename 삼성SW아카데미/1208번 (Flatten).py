for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for _ in range(n):
        max_value = max(arr)
        min_value = min(arr)
        if abs(max_value - min_value) == 1 or abs(max_value - min_value) == 0:
            result = abs(max_value - min_value)
            break
        max_index = arr.index(max_value)
        min_index = arr.index(min_value)
        arr[max_index] -= 1
        arr[min_index] += 1
        result = max(arr) - min(arr)

    print(f"#{test_case} {result}")