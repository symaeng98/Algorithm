from itertools import product

def solution(n, info):
    max_dif = 0
    answer = []
    for p in product([True, False], repeat=11):
        rian_score = [0]*11
        for i in range(11):
            if p[i]:
                rian_score[i] = info[i]+1
        if sum(rian_score) <= n:
            apeach = 0
            rian = 0
            for i in range(11):
                if info[i] == 0 and rian_score[i] == 0:
                    continue
                if p[i]:
                    rian += (10-i)
                else:
                    apeach += (10-i)
            if rian - apeach > max_dif:
                max_dif = rian - apeach
                rian_score[10] += n - sum(rian_score)
                answer = rian_score
            elif max_dif == 0:
                continue
            elif rian - apeach == max_dif:
                for i in range(10, -1, -1):
                    if rian_score[i] > answer[i]:
                        answer = rian_score
                        break
                    elif rian_score[i] == answer[i]:
                        continue
                    else:
                        break
    if max_dif == 0:
        return [-1]
    return answer

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
