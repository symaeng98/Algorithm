from collections import deque
n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
q = deque(arr)
result = []
cnt = 0
while q:
    cnt += 1
    x = q.popleft()
    if cnt == k:
        result.append(str(x))
        cnt = 0
        continue
    q.append(x)

print("<" + ', '.join(result) + ">")