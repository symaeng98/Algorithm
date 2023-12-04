def binary_search(arr, s, e, x):
    if s > e:
        return False
    mid = (s+e) // 2

    if arr[mid] == x:
        return True
    elif arr[mid] < x:
        return binary_search(arr, mid+1, e, x)
    else:
        return binary_search(arr, s, mid-1, x)


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
length = len(a)
a.sort()

for num in b:
    if binary_search(a, 0, length-1, num):
        print("1 ", end="")
    else:
        print("0 ",end="")