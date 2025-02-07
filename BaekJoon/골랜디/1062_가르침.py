from itertools import combinations
#11:03
n, k = map(int, input().split())
k -= 5
alphas = ["a", "n", "t", "i", "c"]
arr = []
for _ in range(n):
    s = ""
    for x in input():
        if x in alphas:
            continue
        s += x
    arr.append(s)

if k < 0:
    print(0)
else:
    r_alphas = ["b", "d", "e", "f", "g", "h", "j", "k", "l", "m", "o", "p",
                "q", "r", "s", "u", "v", "w", "x", "y", "z"]
    result = 0
    for comb in combinations(r_alphas, k):
        now = [0]*26
        cnt = 0
        for c in comb:
            now[ord(c)-ord('a')] = 1

        cnt = 0
        for a in arr:
            tmp = [0]*26
            for s in a:
                tmp[ord(s)-ord('a')] = 1

            flag = False
            for i in range(26):
                if tmp[i] == 1 and now[i] == 0:
                    flag = True
                    break
            if flag:
                continue
            cnt += 1
        result = max(result, cnt)

    print(result)

