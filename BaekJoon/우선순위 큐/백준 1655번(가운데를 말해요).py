##함수 선언 부분
import sys
import heapq
##변수 선언 부분
max_heap = []
min_heap = []
num = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        num = int(sys.stdin.readline())
        if i % 2 == 0: #차례대로 최대 힙과 최소 힙에 넣어준다.
            heapq.heappush(max_heap,-num)
        else:
            heapq.heappush(min_heap,num)
        if i == 0:
            print(-max_heap[0])
        else:
            if -max_heap[0] > min_heap[0]: #최대 힙의 최댓값이 최소 힙의 최솟값보다 크면 서로 교환해준다.
                max_num = -heapq.heappop(max_heap)
                min_num = heapq.heappop(min_heap)
                heapq.heappush(max_heap,-min_num)
                heapq.heappush(min_heap,max_num)
            print(min(min_heap[0],-max_heap[0]))