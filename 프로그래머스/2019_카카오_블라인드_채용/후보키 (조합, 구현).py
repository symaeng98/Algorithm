from itertools import combinations

def solution(relation):
    n = len(relation)
    m = len(relation[0])

    def is_valid(res, arr):
        for i in range(1, len(arr)+1):
            for comb in combinations(arr ,i):
                if list(comb) in res:
                    return False
        return True

    result = []
    for i in range(1, m+1):
        for pro in combinations([i for i in range(m)], i):
            if not is_valid(result, list(pro)):
                continue

            tmp = []
            for j in range(n):
                oy = []
                for p in pro:
                    oy.append(relation[j][p])
                if oy in tmp:
                    break
                tmp.append(oy)

            if len(tmp) == n:
                result.append(list(pro))

    return len(result)