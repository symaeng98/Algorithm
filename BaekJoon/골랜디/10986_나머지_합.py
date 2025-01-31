n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, n):
    arr[i] += arr[i-1]
arr.insert(0, 0)
mod = [0]*m

for a in arr:
    mod[a % m] += 1

result = 0
for x in mod:
    result += x*(x-1)//2

print(result)
# 5 3
# 1 2 3 1 2