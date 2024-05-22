from itertools import combinations

def rec(index, k, now, result, n):
    if index == n//2:
        result.append(sum(now))
        return

    for i in range(6):
        now.append(k[index][i])
        rec(index+1, k, now, result, n)
        now.pop()

def solution(dice):
    n = len(dice)
    answer = []
    max_cnt = -1
    total = 0
    for comb in combinations([i for i in range(n)], n//2):
        a = [dice[i] for i in comb]
        b = []
        for i in [i for i in range(n)]:
            if i not in comb:
                b.append(dice[i])

        a_result = []
        b_result = []
        rec(0, a, [], a_result, n)
        rec(0, b, [], b_result, n)

        # print(a_result)

        a_result.sort(reverse=True)
        b_result.sort(reverse=True)

        m = len(a_result)
        cnt = 0
        ai = 0
        bi = 0
        while ai < m and bi < m:
            if a_result[ai] <= b_result[bi]:
                bi += 1
            else:
                cnt += (m-bi)
                ai += 1


        if max_cnt < cnt:
            max_cnt = cnt
            answer = list(comb)

    for i in range(len(answer)):
        answer[i] += 1

    return answer