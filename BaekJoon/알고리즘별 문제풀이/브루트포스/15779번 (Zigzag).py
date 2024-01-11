n = int(input())
arr = list(map(int, input().split()))

if n <= 2:
    print(n)
else:
    max_length = -1
    length = 3
    for i in range(n-2):
        if arr[i] <= arr[i+1] <= arr[i+2] or arr[i+2] <= arr[i+1] <= arr[i]:
            max_length = max(max_length, length-1)
            length = 3
            continue
        length += 1

    max_length = max(max_length, length-1)
    print(max_length)