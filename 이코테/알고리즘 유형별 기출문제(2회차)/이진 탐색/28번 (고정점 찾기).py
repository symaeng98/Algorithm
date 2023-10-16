# 5
# -12 -3 1 3 10 11 12
#  0   1 2 3 4   5  6
n = int(input())
arr = list(map(int, input().split()))

def binary_search(start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binary_search(start, mid-1)
    else:
        return binary_search(mid+1, end)

result = binary_search(0, n-1)
if result == None:
    print(-1)
else:
    print(result)