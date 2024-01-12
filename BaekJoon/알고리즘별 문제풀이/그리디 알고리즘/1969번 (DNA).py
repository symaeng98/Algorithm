n, m = map(int, input().split())
arr = [input() for _ in range(n)]
result = []
hm_dist = 0
for i in range(m):
    dna_dict = {"A": 0, "T": 0, "G": 0, "C": 0}
    for a in arr:
        dna_dict[a[i]] += 1
    sd = sorted(dna_dict.items(), key=lambda x:(-x[1], x[0]))
    result.append(sd[0][0])
    hm_dist += (n - sd[0][1])

print(''.join(result))
print(hm_dist)