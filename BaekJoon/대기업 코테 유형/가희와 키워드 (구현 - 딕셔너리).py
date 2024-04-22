import sys
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())
memo_keyword = defaultdict(bool)

for _ in range(n):
    word = input().rstrip()
    memo_keyword[word] = True

length = n
for _ in range(m):
    write_keyword = list(input().rstrip().split(","))
    for wk in write_keyword:
        if wk in memo_keyword.keys():
            if memo_keyword[wk]:
                memo_keyword[wk] = False
                length -= 1

    print(length)
