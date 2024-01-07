n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k == 1:
    print(arr[n-1] - arr[0])
else:
    arr_dif = []
    for i in range(1, n):
        arr_dif.append((arr[i] - arr[i-1], i))

    indexes = []
    for a in sorted(arr_dif, reverse=True):
        indexes.append(a[1])

    indexes = indexes[:k-1]
    indexes.sort()

    result = []
    l = 0
    for i in indexes:
        result.append(arr[i-1] - arr[l])
        l = i
    result.append(arr[-1] - arr[indexes[-1]])

    print(sum(result))
