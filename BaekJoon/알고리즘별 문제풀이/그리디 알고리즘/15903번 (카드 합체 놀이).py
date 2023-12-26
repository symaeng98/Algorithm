import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

q = []
for i in range(len(arr)):
    heapq.heappush(q, (arr[i], i))

for _ in range(m):
    x1, i1 = heapq.heappop(q)
    x2, i2 = heapq.heappop(q)
    sum_value = x1 + x2
    arr[i1] = sum_value
    arr[i2] = sum_value
    heapq.heappush(q, (sum_value, i1))
    heapq.heappush(q, (sum_value, i2))

print(sum(arr))