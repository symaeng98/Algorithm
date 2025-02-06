import heapq

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

lectures.sort()

room_end_time = []
heapq.heappush(room_end_time, lectures[0][1])

for i, (start, end) in enumerate(lectures):
    if i == 0:
        continue
    if room_end_time[0] <= start:
        heapq.heappop(room_end_time)
    heapq.heappush(room_end_time, end)

print(len(room_end_time))

# 3
# 1 3
# 2 4
# 3 5

# 9
# 1 3
# 3 5
# 5 10
# 2 7
# 7 9
# 4 9
# 9 12
# 8 10
# 6 11