from collections import defaultdict

n = int(input())
words = list(input() for _ in range(n))
words.sort(key=lambda x: -len(x))
count_map = defaultdict(int)

for word in words:
    for i in range(len(word)):
        count_map[word[i]] += 10**(len(word)-i-1)

alpha_map = defaultdict(int)
now = 9
result = 0
for w, value in sorted(count_map.items(), key=lambda x: -x[1]):
    result += value*now
    now -= 1

print(result)
# 2
# GCF
# ACDEB