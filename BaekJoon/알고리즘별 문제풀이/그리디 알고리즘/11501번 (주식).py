import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max_value = -1
    result = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_value:
            max_value = arr[i]
        else:
            result += max_value-arr[i]

    print(result)