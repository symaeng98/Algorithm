import heapq
n = int(input())

q = []

for _ in range(n):
    start, end = map(int, input().split())
    q.append((start, end))

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if room[0] <= q[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, q[i][1])

print(len(room))