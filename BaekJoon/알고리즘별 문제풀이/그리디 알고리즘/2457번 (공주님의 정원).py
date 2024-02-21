n = int(input())
arr = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    arr.append([sm * 100 + sd, em * 100 + ed])

arr.sort()

end = 301

cnt = 0

while arr:
    if end >= 1201 or arr[0][0] > end:
        break

    tmp = -1
    for _ in range(len(arr)):
        if arr[0][0] <= end:
            if tmp <= arr[0][1]:
                tmp = arr[0][1]
            arr.remove(arr[0])
        else:
            break

    end = tmp
    cnt += 1

if end < 1201:
    print(0)
else:
    print(cnt)
