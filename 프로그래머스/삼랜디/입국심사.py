def check(times, n, x):
    people = 0
    for t in times:
        people += x // t

    if people >= n:
        return True
    return False

def solution(n, times):
    # 가능한 최솟값과 최댓값을 left와 right로 설정
    left = 0
    right = max(times) * n+1

    # 이분탐색이니 left가 right 이하인 동안
    while left+1 < right:
        # 가운데 : 더하고 2로 나눈 몫(정수)
        mid = (left+right)//2
        # 심사한 사람 수
        people = 0

        for time in times:
            # 해당 심사대에서 주어진 시간동안 심사 받은 수 더하기
            people += mid//time

        # n명 초과 심사했다면, 시간이 너무 많은 것
        # 딱 n명 심사했더라도, 시간이 남을 가능성 있음
        if people >= n:
            right = mid
        # n명 미만 심사했다면, 시간이 너무 부족하다
        else :
            left = mid

    if check(times, n, left):
        return left
    else:
        return right