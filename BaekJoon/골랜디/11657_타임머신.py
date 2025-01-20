INF = 1e9
n, m = map(int, input().split())
edges = []
distance = [INF]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bellman_ford(s):
    distance[s] = 0
    for i in range(n):  # 음수 순환 판단을 위해 1번 더 돌림 (원래는 n-1번 돌림)
        for start, end, cost in edges:
            if distance[start] != INF:
                if distance[end] > distance[start]+cost:
                    distance[end] = distance[start]+cost
                    if i == n-1:  # 1번 더 돌렸을 때 갱신이 되면, 음수 순환이 존재하는 것임
                        return False

    return True


if bellman_ford(1):
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)
# 3 4
# 1 2 4
# 1 3 3
# 2 3 -1
# 3 1 -2