from collections import deque
def solution(A, B):
    A.sort()
    B.sort()
    bq = deque(B)
    cnt = 0
    for i in range(len(A)-1, -1, -1):
        if A[i] >= bq[-1]:
            bq.popleft()
        else:
            bq.pop()
            cnt += 1
    return cnt