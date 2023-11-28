import heapq

n, k = map(int, input().split())

jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))
jewels.sort()

bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()

tmp = []
result = 0
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(tmp, -jewels[0][1])
        heapq.heappop(jewels)
    if tmp:
        result -= heapq.heappop(tmp)

print(result)