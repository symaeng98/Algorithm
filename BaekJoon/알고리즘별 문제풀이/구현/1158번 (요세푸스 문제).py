n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
result = []
index = 0

for i in range(n):
    index = (index + k-1) % len(arr)
    result.append(str(arr.pop(index)))

print("<" + ', '.join(result) + ">")