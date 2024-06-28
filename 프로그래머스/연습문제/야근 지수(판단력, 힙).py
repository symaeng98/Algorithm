import heapq
def solution(n, works):
    answer = 0
    hq = []
    for work in works:
        hq.append(-work)
    heapq.heapify(hq)
    while hq[0] != 0 and n > 0:
        heapq.heappush(hq, heapq.heappop(hq)+1)
        n -= 1
    for data in hq:
        answer += data**2
    return answer