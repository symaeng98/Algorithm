n, x = map(int,input().split())
arr = list(map(int, input().split()))

def first(start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == x and (mid == 0 or x > arr[mid-1]):
        return mid
    elif arr[mid] >= x:
        return first(start, mid-1)
    else:
        return first(mid+1, end)

def last(start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == x and (mid == n-1 or x < arr[mid+1]):
        return mid
    elif arr[mid] > x:
        return last(start, mid-1)
    else:
        return last(mid+1, end)

f = first(0, n-1)
l = last(0, n-1)
if f == -1 or l == -1:
    print(-1)
else:
    print(l-f+1)

# 7 2
# 1 1 2 2 2 2 3

# 7 4
# 1 1 2 2 2 2 3