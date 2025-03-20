#08:23
from itertools import combinations, permutations
def solution(user_id, banned_id):
    answer = 0
    n = len(user_id)
    m = len(banned_id)

    def check(names):
        def name_check(name, b_name):
            if len(name) != len(b_name):
                return False

            for i in range(len(name)):
                if b_name[i] == "*":
                    continue
                if name[i] != b_name[i]:
                    return False

            return True

        for perm in permutations(names):
            flag = True
            for i in range(m):
                if not name_check(perm[i], banned_id[i]):
                    flag = False
            if flag:
                return True

        return False

    for comb in combinations(user_id, m):
        if check(comb):
            answer += 1

    return answer
