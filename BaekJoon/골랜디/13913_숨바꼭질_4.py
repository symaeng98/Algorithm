from collections import deque

n, k = map(int, input().split())

parent = [-1]*100001

q = deque()
q.append((0, n))
parent[n] = n
while q:
    cnt, now = q.popleft()
    if now == k:
        print(cnt)
        break

    for x in [now+1, now*2, now-1]:
        if 0 <= x <= 100000 and parent[x] == -1:
            parent[x] = now
            q.append((cnt+1, x))


x = k
result = [k]
while x != n:
    x = parent[x]
    result.append(x)

result.reverse()
print(*result)
