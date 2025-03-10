n, m = map(int, input().split())
tps = list(map(int, input().split()))
tps.pop(0)
parent = [i for i in range(n+1)]
parties = [list(map(int, input().split())) for _ in range(m)]
for party in parties:
    party.pop(0)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for party in parties:
    for i in range(len(party)-1):
        union(party[i], party[i+1])

for i in range(1, n+1):
    parent[i] = find_parent(i)

tmp = []
for t in tps:
    tmp.append(parent[t])

tps.extend(tmp)
tps = set(tps)

lps = []
for i in range(1, n+1):
    if parent[i] in tps:
        continue
    lps.append(i)

result = 0
for party in parties:
    fail = False
    for p in party:
        if p not in lps:
            fail = True
    if not fail:
        result += 1

print(result)

# 10 9
# 4 1 2 3 4
# 2 1 5
# 2 2 6
# 1 7
# 1 8
# 2 7 8
# 1 9
# 1 10
# 2 3 10
# 1 4
