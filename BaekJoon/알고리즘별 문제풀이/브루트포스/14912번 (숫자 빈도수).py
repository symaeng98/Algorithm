n, k = map(int, input().split())
arr = [str(i) for i in range(1, n+1)]
s = ''.join(arr)
print(s.count(str(k)))