def bellman_ford():
    for i in range(n):  # 음수 순환 판단을 위해 1번 더 돌림 (원래는 n-1번 돌림)
        for start, end, cost in edges:
            if distance[end] > distance[start]+cost:
                distance[end] = distance[start]+cost
                if i == n-1:  # 1번 더 돌렸을 때 갱신이 되면, 음수 순환이 존재하는 것임
                    return True

    return False


INF = 1e9
t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    edges = []
    distance = [INF]*(n+1)
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    if bellman_ford():
        print("YES")
    else:
        print("NO")
