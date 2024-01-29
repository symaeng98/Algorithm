n, m = map(int, input().split())
result = [0]*(n+1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        result[x] = k

for r in result[1:n+1]:
    print(r, end=" ")