from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append((i, j))
        if graph[i][j] == 1:
            houses.append((i, j))

min_result = 1e9
for comb in combinations(chickens, m):
    for chicken in chickens:
        if chicken in comb:
            continue
        graph[chicken[0]][chicken[1]] = 0

    min_sum = 0
    for i, j in houses:
        min_tmp = 1e9
        for k, l in comb:
            min_tmp = min(min_tmp, abs(i-k)+abs(j-l))
        min_sum += min_tmp

    min_result = min(min_result, min_sum)

    for i, j in comb:
        graph[i][j] = 2

print(min_result)

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2