import sys
import heapq

n = int(sys.stdin.readline())
max_hp = []
min_hp = []
for i in range(n):
    x = int(sys.stdin.readline())
    if i % 2 == 0:
        heapq.heappush(max_hp, -x)
    else:
        heapq.heappush(min_hp, x)

    if i == 0:
        print(-max_hp[0])
        continue

    if -max_hp[0] > min_hp[0]:
        mx = -heapq.heappop(max_hp)
        mn = heapq.heappop(min_hp)
        heapq.heappush(max_hp, -mn)
        heapq.heappush(min_hp, mx)

    print(-max_hp[0])
