x, y = map(int, input().split())

now = int(y*100/x)

start = 0
end = 1000000000

def check(k):
    if int(((y+k)*100)/(x+k)) >= (now+1):
        return True
    return False


while start+1 < end:
    mid = (start + end) // 2
    if check(mid):
        end = mid
    else:
        start = mid

if check(end):
    print(end)
else:
    print(-1)
