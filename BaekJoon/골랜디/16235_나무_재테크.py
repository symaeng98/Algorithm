from collections import defaultdict

n, m, k = map(int, input().split())
graph = [[5]*n for _ in range(n)]
growth = [list(map(int, input().split())) for _ in range(n)]
die_growth = defaultdict(int)
tree = defaultdict(list)
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[n*(x-1)+(y-1)].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]

year = 0
while True:
    if year == k:
        break

    for i in range(n):
        for j in range(n):
            if tree[n*i+j]:
                trees = tree[n*i+j]
                trees.sort()
                die_index = -1
                for index, t in enumerate(trees):
                    if t <= graph[i][j]:
                        graph[i][j] -= t
                        trees[index] += 1
                        continue
                    die_index = index
                    break

                if die_index != -1:
                    # print(f"{i}, {j} 죽기 시작 인덱스:", die_index)
                    # print(f"{i}, {j} 죽기 전:", graph[i][j], tree[n*i+j])
                    for dg in trees[die_index:]:
                        die_growth[n*i+j] += dg // 2
                    # print("죽고 난 양분:", die_growth[n*i+j])
                    tree[n*i+j] = trees[:die_index]
                    # print(f"{i}, {j} 죽은 뒤:", graph[i][j], tree[n*i+j])

    for i in range(n):
        for j in range(n):
            graph[i][j] += die_growth[n*i+j]
            die_growth[n*i+j] = 0

    for i in range(n):
        for j in range(n):
            if tree[n*i+j]:
                trees = tree[n*i+j]
                for t in trees:
                    if t % 5 == 0:
                        for l in range(8):
                            nx = i + dx[l]
                            ny = j + dy[l]
                            if 0 <= nx < n and 0 <= ny < n:
                                tree[n*nx+ny].append(1)

            graph[i][j] += growth[i][j]

    year += 1

result = 0
for i in range(n):
    for j in range(n):
        if tree[n*i+j]:
            result += len(tree[n*i+j])

print(result)

# 5 2 1
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 1 3
# 3 2 3