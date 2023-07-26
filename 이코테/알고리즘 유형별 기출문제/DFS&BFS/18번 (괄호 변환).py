def solution(p):
    answer = ''
    if p == '':
        return answer
    u, v = divide(p)
    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

def divide(pStr):
    cnt = 0
    for ind, p in enumerate(pStr):
        if p == '(':
            cnt -= 1
        else:
            cnt += 1
        if cnt == 0:
            return (pStr[:ind+1], pStr[ind+1:])


def check(pStr):
    cnt = 0
    for p in pStr:
        if p == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True