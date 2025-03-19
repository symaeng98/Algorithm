def solution(A, B):
    A.sort(reverse=True)
    B.sort()
    answer = 0
    for a in A:
        if B and B[-1] > a:
            B.pop()
            answer += 1

    return answer