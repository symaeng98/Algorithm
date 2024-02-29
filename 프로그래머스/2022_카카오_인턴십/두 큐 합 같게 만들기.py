from collections import deque

def solution(queue1, queue2):
    k = (sum(queue1) + sum(queue2)) // 2
    q1 = deque(queue1)
    q2 = deque(queue2)

    cnt = 0
    now = sum(q1)
    while True:
        if not q1 or not q2:
            break
        if cnt > 3*len(queue1):
            break
        if now == k:
            return cnt
        elif now > k:
            x = q1.popleft()
            q2.append(x)
            now -= x
        else:
            x = q2.popleft()
            q1.append(x)
            now += x

        cnt += 1

    return -1
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))