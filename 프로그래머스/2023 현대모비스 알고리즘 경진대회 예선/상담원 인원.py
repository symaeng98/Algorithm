from itertools import combinations_with_replacement
def solution(k, n, reqs):
    req_type = [i for i in range(1, k+1)]
    req_list = [[] for _ in range(k+1)]
    for a, b, c in reqs:
        req_list[c].append((a, b))
    for i in range(1, len(req_list)):
        req_list[i].sort()

    def get_wait_time(r_list, cnt):
        if not r_list:
            return 0
        finish = [0]*cnt
        wait_time = 0
        for s, t in r_list:
            i = finish.index(min(finish))
            if finish[i] <= s:
                finish[i] = s+t
            else:
                wait_time += finish[i] - s
                finish[i] += t

        return wait_time

    answer = []
    for cr in combinations_with_replacement(req_type, n-k):
        cnt_list = [1]*(k+1)
        for c in cr:
            cnt_list[c] += 1

        result = 0
        for i in range(1, k+1):
            result += get_wait_time(req_list[i], cnt_list[i])
        answer.append(result)

    return min(answer)