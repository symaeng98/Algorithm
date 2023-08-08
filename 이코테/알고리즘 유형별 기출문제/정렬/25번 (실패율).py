def solution(N, stages):
    users = len(stages)
    answer = []

    for i in range(1,N+1):
        count = stages.count(i)
        if users == 0:
            fail = 0
        else:
            fail = count/users
        answer.append((i, fail))
        users -= count
    answerSort = sorted(answer, key=lambda x: -x[1])

    return [a[0] for a in answerSort]