def solution(n, s):
    answer = [1]*n
    cnt = s-n
    if cnt < 0:
        return [-1]
    a = cnt//n
    b = cnt%n
    for i in range(n):
        answer[i] += a

    for i in range(b):
        answer[n-1-i] += 1

    return answer