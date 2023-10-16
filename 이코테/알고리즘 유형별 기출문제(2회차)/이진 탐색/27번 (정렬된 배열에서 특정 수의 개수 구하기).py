# 7 2
# 1 1 1 1 2 2 2 3
n, k = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search_left(start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == k and (mid == 0 or arr[mid-1] < k):
        return mid
    elif arr[mid] >= k:
        return binary_search_left(start, mid-1)
    else:
        return binary_search_left(mid+1, end)

def binary_search_right(start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == k and (mid == n-1 or arr[mid+1] > k):
        return mid
    elif arr[mid] > k:
        return binary_search_right(start, mid-1)
    else:
        return binary_search_right(mid+1, end)

l = binary_search_left(0, n-1)
r = binary_search_right(0, n-1)

if l == None or r == None:
    print(-1)
else:
    print(r-l+1)