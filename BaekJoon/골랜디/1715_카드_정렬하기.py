import heapq
n = int(input())
min_hp = []
for _ in range(n):
    heapq.heappush(min_hp, int(input()))

result = 0
while min_hp:
    x = heapq.heappop(min_hp)
    if not min_hp:
        break
    y = heapq.heappop(min_hp)

    result += x+y
    heapq.heappush(min_hp, x+y)

print(result)

# 3
# 10
# 20
# 40