import heapq

N = int(input())

heap = []
for i in range(N):
    num = int(input())
    heapq.heappush(heap, num)

result = 0
while len(heap) != 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    sumValue = num1 + num2
    result += sumValue
    heapq.heappush(heap, sumValue)
print(result)