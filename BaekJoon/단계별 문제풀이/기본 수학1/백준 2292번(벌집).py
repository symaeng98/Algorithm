##함수 선언 부분##

##변수 선언 부분##
N = 0
cnt = 1
num = 0
six = 6
##메인 함수 부분##
if __name__ == "__main__" :
    N = int(input())
    while True :
        if N == 1:
            print(1) ##벌집의 가운데는 1
            break

        elif N >= six * num + 2 : ##six를 6으로 미리 정해두었다
            num += cnt
            cnt += 1
            if N <= six * num + 1 :
                print(cnt)
                break

##가운데에서 멀어질 수록 증가량이 어느정도 되는지 구하는 문제
##간단한 패턴만 찾으면 쉽게 풀 수 있다.

