def solution(edges):
    n = -1
    for a, b in edges:
        n = max(n, a, b)

    in_degree = [[] for _ in range(n+1)]
    out_degree = [[] for _ in range(n+1)]
    for a, b in edges:
        out_degree[a].append(b)
        in_degree[b].append(a)

    total = 0
    dot = 0
    for i in range(1, n+1):
        if len(in_degree[i]) == 0 and len(out_degree[i]) >= 2:
            dot = i
            total = len(out_degree[i])
            break

    answer = [dot, 0, 0, 0]
    for i in range(1, n+1):
        if len(out_degree[i]) == 0 and len(in_degree[i]) != 0:
            answer[2] += 1
        if len(out_degree[i]) == 2:
            if len(in_degree[i]) >= 2:
                answer[3] += 1

    print(total, answer)
    answer[1] = total-sum(answer[2:])

    return answer