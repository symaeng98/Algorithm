import heapq
def solution(operations):
    cnt = 0
    min_heap = []
    max_heap = []
    for operation in operations:
        oper, tmp = operation.split(" ")
        n = int(tmp)
        if oper == "I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            cnt += 1
        elif oper == "D":
            if cnt == 0:
                continue
            if n == -1:
                heapq.heappop(min_heap)
            elif n == 1:
                heapq.heappop(max_heap)
            cnt -= 1
        if cnt == 0:
            max_heap = []
            min_heap = []

    if cnt == 0:
        return [0, 0]

    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]