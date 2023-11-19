##함수 선언 부분##

##변수 선언 부분##
M = 0
N = 0
min = 0
sum = 0
isRight = 0
##메인 함수 부분##
if __name__ == "__main__":
    M = int(input())
    N = int(input())
    for i in range(M, N+1):
        isRight = 0 #소수가 맞는지 판별해준다.
        for j in range(2, i):
            if i % j == 0: #2부터 자기 자신 - 1 까지 나누어 주어서 나누어 떨어지면
                isRight = 0 #소수가 아니다
                break #반복문 탈출

            isRight = 1 #그게 아니라면 소수다

        if isRight == 1 or i == 2: #2가 누락이 되므로 2인 경우만 포함해준다.
            if sum == 0: #소수를 구했지만 sum이 0이라는 것은 첫번째 경우이기 때문에
                min = i
            sum += i
    if sum == 0:
        print(-1)
    else:
        print(sum)
        print(min)


    ##그렇게 어렵지 않은 문제였지만, sum이 0인 경우가 첫번째 경우인 것을 파악하지 못하면
    ##어려울 수 있는 문제였다.