from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for inf in info:
        s_info = inf.split()
        condition = s_info[:-1]
        score = int(s_info[-1])
        for i in range(5):
            for c in combinations([0, 1, 2, 3], i):
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                info_dict[key].append(score)

    for value in info_dict.values():
        value.sort()


    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        target_key = ''.join(q[:-1])
        target_score = int(q[-1])

        cnt = 0
        if target_key in info_dict:
            target_list = info_dict[target_key]
            idx = bisect_left(target_list, target_score)
            cnt = len(target_list) - idx
        answer.append(cnt)
    return answer

print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
