##함수 선언 부분##

##변수 선언 부분##
X = 0
List = []
num = 0
cnt = 0
##메인 함수 부분##
if __name__ == "__main__" :
    X = int(input())

    while cnt < X :
        num += 1
        cnt += num

    cnt -= num

    if num % 2 == 0: ##짝수일 때와 홀수일 때 계산방법이 반대다
        i = X - cnt
        j = num - i + 1
    else :
        j = X - cnt
        i = num - j + 1

    print(f"{i}/{j}")

##대각선으로 값을 차례대로 이동하면서 입력값에 맞게 찾는 문제다.
##무한 루프안에서 for문 하나 써서 풀었는데 백준에서는 시간초과라
##좀 더 수학적인 관점에서 접근했다. 어렵진 않은데 시간 제한이 있으면
##당황했을 것 같다.