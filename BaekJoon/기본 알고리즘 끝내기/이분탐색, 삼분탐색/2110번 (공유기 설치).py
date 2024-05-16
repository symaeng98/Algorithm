n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start, end = 1, arr[-1] - arr[0]

def check(length):
    cnt = 1
    now = arr[0]
    for a in arr:
        if a >= now + length:
            cnt += 1
            now = a

    if cnt >= c:
        return True

    return False


while start + 1 < end:
    mid = (start + end) // 2
    if check(mid):
        start = mid
    else:
        end = mid

if check(end):
    print(end)
else:
    print(start)