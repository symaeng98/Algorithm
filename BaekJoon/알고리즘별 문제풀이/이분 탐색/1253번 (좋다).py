n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(n):
    new_arr = arr[:i] + arr[i + 1:]
    start, end = 0, len(new_arr) - 1
    while start < end:
        x = new_arr[start] + new_arr[end]
        if x == arr[i]:
            ans += 1
            break
        if x < arr[i]:
            start += 1
        else:
            end -= 1

print(ans)