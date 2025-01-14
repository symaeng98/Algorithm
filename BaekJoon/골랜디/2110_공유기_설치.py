n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()


def check(x):
    cnt = 1
    now = arr[0]
    for a in arr:
        if now + x <= a:
            now = a
            cnt += 1

    if cnt < c:
        return False
    return True


start, end = 0, arr[-1] - arr[0] + 1
while start + 1 < end:
    mid = (start + end)//2
    if check(mid):
        start = mid
    else:
        end = mid


if check(start):
    print(start)
else:
    print(end)
