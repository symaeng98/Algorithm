n = int(input())
arr = list(map(int, input().split()))
arr.sort()


def bs(start, end, x):
    l, r = start, end
    while start + 1 < end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid
        else:
            end = mid

    if start == l:
        return end
    elif end == r:
        return start
    else:
        if abs(x-arr[start]) < abs(x-arr[end]):
            return start
        else:
            return end


# print(arr)
tmp = 4000000000
result = [0, 0, 0]
for i in range(n-2):
    for j in range(i+1, n-1):
        start = j+1
        end = n-1
        x = -(arr[i] + arr[j])
        p = bs(j, n, x)
        # print(arr[i], arr[j], x, p)

        if tmp > abs(arr[i]+arr[j]+arr[p]):
            tmp = abs(arr[i]+arr[j]+arr[p])
            result = [arr[i], arr[j], arr[p]]

print(*result)
# 5
# -2 6 -97 -6 98