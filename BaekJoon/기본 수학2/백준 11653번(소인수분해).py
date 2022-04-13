##함수 선언 부분##

##변수 선언 부분##
N = 0
arr = []
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    while N != 1: #N이 1이 될 때 까지 나누어 준다.
        for i in range(2, N+1): #2부터 자기자신까지
            if N % i == 0 : #나누어 떨어지면
                N //= i #나누어주고
                arr.append(i) #나눈 값을 arr뒤에 붙여준다.
                break

    for i in arr:
        print(i)

#코드를 간단히 짠 것 같다. 소인수분해의 원리만 알면 쉬운 문제