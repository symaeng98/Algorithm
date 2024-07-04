def solution(n, costs):
    parent = [i for i in range(n)]
    def find_parent(x):
        if parent[x] == x:
            return x
        return find_parent(parent[x])

    def union_parent(a, b):
        a = find_parent(a)
        b = find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    result = 0
    for v1, v2, c in sorted(costs, key=lambda x:(x[2])):
        if find_parent(v1) == find_parent(v2):
            continue
        union_parent(v1, v2)
        result += c

    return result