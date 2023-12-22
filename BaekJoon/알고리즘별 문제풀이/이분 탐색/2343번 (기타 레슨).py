def bs(arr, m, start, end):
    while start + 1 < end:
        mid = (start + end) // 2
        if check(arr, mid, m):
            end = mid
        else:
            start = mid

    if check(arr, start, m):
        return start
    return end


def check(arr, x, m):
    cnt = 1
    sum_value = 0
    for a in arr:
        sum_value += a
        if sum_value > x:
            sum_value = a
            cnt += 1

    if cnt > m:
        return False

    return True


n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)


print(bs(arr, m, start, end))