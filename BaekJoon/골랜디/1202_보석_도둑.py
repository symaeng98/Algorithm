import heapq

n, k = map(int, input().split())
arr = []
jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))
jewels.sort(reverse=True)

for _ in range(k):
    c = int(input())
    arr.append(c)
arr.sort()

tmp = []
result = 0
for a in arr:
    while jewels and jewels[-1][0] <= a:
        m, v = jewels.pop()
        heapq.heappush(tmp, -v)
    if tmp:
        result += -heapq.heappop(tmp)

print(result)

# 3 2
# 1 65
# 5 23
# 2 99
# 10
# 2