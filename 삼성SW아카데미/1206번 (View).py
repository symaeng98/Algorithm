for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        left = 255
        right = 255
        for l in range(1, 3):
            left = min(left, arr[i]-arr[i-l])
        for r in range(1, 3):
            right = min(right, arr[i]-arr[i+r])
        if left < 0 or right < 0:
            continue
        result += min(left, right)

    print(f"#{test_case} {result}")