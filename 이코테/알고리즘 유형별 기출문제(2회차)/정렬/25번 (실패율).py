def solution(N, stages):
    answer = []
    dic = {}
    num = len(stages)
    for i in range(1,N+1):
        if num == 0:
            dic[i] = 0
            continue
        cnt = stages.count(i)
        dic[i] = cnt / num
        num -= cnt
    a = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    for c,v in a:
        answer.append(c)

    return answer