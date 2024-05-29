from collections import defaultdict

def solution(gems):
    all_gems = set(gems)
    cnt_dict = defaultdict(int)

    end = 0
    min_start, min_end = 0, 0
    min_length = 1e9

    for start in range(len(gems)):
        while len(cnt_dict.keys()) != len(all_gems) and end < len(gems):
            cnt_dict[gems[end]] += 1
            end += 1
        if len(cnt_dict.keys()) == len(all_gems):
            if min_length > end-start+1:
                min_length = end-start+1
                min_start = start
                min_end = end

        cnt_dict[gems[start]] -= 1
        if cnt_dict[gems[start]] == 0:
            del(cnt_dict[gems[start]])

    return [min_start+1, min_end]