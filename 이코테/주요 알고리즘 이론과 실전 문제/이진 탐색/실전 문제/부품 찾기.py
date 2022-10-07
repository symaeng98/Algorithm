def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if (arr[mid] == target):
            return True
        elif (arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return False


n = int(input())
nList = list(map(int,input().split()))
m = int(input())
mList = list(map(int,input().split()))

nList.sort()
for m in mList:
    if binary_search(nList, m, 0, n-1):
        print("yes",end=" ")
    else:
        print("no",end=" ")