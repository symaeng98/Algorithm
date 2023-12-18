n = int(input())
k = int(input())
arr = list(map(int, input().split()))

if n <= k:
    print(0)
else:
    arr.sort()

    dist_dif = []
    for i in range(1, len(arr)):
        dist_dif.append(arr[i] - arr[i-1])

    dist_dif.sort(reverse=True)
    print(sum(dist_dif[k-1:]))
