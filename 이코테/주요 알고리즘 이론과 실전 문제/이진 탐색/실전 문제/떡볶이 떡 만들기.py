def cut(list, len):
    sum = 0
    for l in list:
        if l < len:
            continue
        sum += l - len
    return sum


N, M = map(int, input().split(" "))
x = list(map(int, input().split(" ")))

start = 0
end = max(x)
ans = 0
while start<=end:
    mid = (start+end)//2
    if cut(x, mid) < M:
        end = mid-1
    else:
        ans = mid
        start = mid+1

print(ans)