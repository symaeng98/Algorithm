N = int(input())
arr = list(map(int, input().split()))

def bs(start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return bs(mid+1, end)
    else:
        return bs(start, mid-1)

print(bs(0,N))