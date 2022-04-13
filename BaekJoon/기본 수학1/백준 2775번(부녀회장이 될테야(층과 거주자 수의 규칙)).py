##함수 선언 부분##

##변수 선언 부분##
T = 0
k = 0
n = 0
people = 0
##메인 함수 부분##
if __name__ == "__main__" :
    T = int(input())
    for i in range(0, T):
        k = int(input())
        n = int(input())
        people = [i for i in range(1, n+1)]  ##파이썬의 편리함을 알 수 있는
                                             ##for문 안에서 i 대입

        for j in range(k):
            for l in range(1, n):
                people[l] += people[l-1]  ## 그 전 호수의 사람인원을 더해준다.
        print(people[n-1])

##생각보다 재귀함수보다 코드가 짧게 나온다.
##인터넷의 도움을 받았던 문제
##수학적인 규칙은 찾았지만 구현하기가 힘들었다.
##리스트 하나에 그 전 수를 더해주는 느낌으로 진행한다. 피보나치 느낌