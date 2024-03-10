from itertools import permutations
def solution(k, dungeons):
    max_cnt = -1
    for per in permutations(dungeons):
        now = k
        cnt = 0
        for minimum, used in per:
            if now < minimum:
                break
            now -= used
            cnt += 1
        max_cnt = max(max_cnt, cnt)

    return max_cnt

print(solution(80, [[80,20],[50,40],[30,10]]))