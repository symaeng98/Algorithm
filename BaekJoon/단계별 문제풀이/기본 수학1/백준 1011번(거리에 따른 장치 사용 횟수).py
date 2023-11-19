##함수 선언 부분##

##변수 선언 부분##
T = 0
X = 0
Y = 0
distance = 0
cnt = 0
move = 1
move_plus = 0
##메인 함수 부분##
if __name__ == "__main__" :
    T = int(input())
    for i in range(0, T): #T번의 테스트 케이스
        X, Y = map(int, input().split())
        distance = Y - X
        cnt = 0
        move = 1
        move_plus = 0
        while move_plus < distance:
            cnt += 1
            move_plus += move #cnt에 해당하는 move만큼 이동거리의 합에 더해준다.
            if cnt % 2 == 0 : #2,2 3,3 4,4 5,5 ... 식으로 cnt의 빈도가 늘어나기 때문에
                move += 1 #2번에 한번씩 move를 1씩 증가시켜준다.

        print(cnt)



##시간 초과때문에 애를 많이 먹은 문제였다. 시간초과가 왜 나오는 지 이해가 잘 안갔지만 아마 반복문을
##계속해서 돌기 때문인 것 같다. 구글링해서 찾은 이 문제의 해답은 나처럼 1부터 distance까지
##반복하는 것이 아니라 cnt값을 1씩 증가시키면서 이동거리의 합의 최대값을 이용하는 것이었다.
##규칙은 쉽게 찾았지만 그에 따른 변수 설정이 어렵고 실행속도에서 overflow가 발생했던 문제다.