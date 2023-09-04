n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr_sorted = sorted(arr, key=lambda x:(-(str(bin(x)[2:]).count("1")), -x))
print(arr_sorted[k-1])