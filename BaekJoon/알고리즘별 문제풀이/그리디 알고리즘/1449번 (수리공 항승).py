n, l = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

start = arr[0]
result = 1
for i in range(1, len(arr)):
    if arr[i] not in range(start, start+l):
        start = arr[i]
        result += 1

print(result)
