##함수 선언 부분
def merge_sort(ar, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(ar, left, mid)
        merge_sort(ar, mid+1, right)
        merge(ar, left, mid, right)

def merge(ar, left, mid, right):
    i = left
    j = mid + 1
    k = left
    _sorted = [0] * len(ar)
    while i <= mid and j <= right:
        if ar[i] <= ar[j]:
            _sorted[k] = ar[i]
            k += 1
            i += 1
        else:
            _sorted[k] = ar[j]
            k += 1
            j += 1
    if i > mid:
        for l in range(j,right+1):
            _sorted[k] = ar[l]
            k += 1
    else:
        for l in range(i,mid+1):
            _sorted[k] = ar[l]
            k += 1
    for l in range(left, right+1):
        ar[l] = _sorted[l]

##변수 선언 부분
arr = []

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        arr.append(int(input()))
    merge_sort(arr, 0, N-1)
    for i in range(N):
        print(arr[i])