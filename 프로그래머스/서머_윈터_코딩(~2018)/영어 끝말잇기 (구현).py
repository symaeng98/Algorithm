from collections import defaultdict
def solution(n, words):
    used = []
    cnt_dict = defaultdict(int)
    for i in range(len(words)):
        cnt_dict[i%n] += 1
        if i != 0 and words[i-1][-1] != words[i][0]:
            return [i%n+1, cnt_dict[i%n]]
        if words[i] in used:
            return [i%n+1, cnt_dict[i%n]]
        used.append(words[i])

    return [0, 0]