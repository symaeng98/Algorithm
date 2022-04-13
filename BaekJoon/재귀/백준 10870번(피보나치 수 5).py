##함수 선언 부분
def fibonacci(num):
    if num == 0: #초기값 설정 F_0은 0으로
        return 0
    elif num == 1: #F_1은 1로 설정한다
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

##변수 선언 부분
N = 0
asn = 0

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    ans = fibonacci(N)
    print(ans)

#피보나치를 잘 이해하고 있으면 어렵지 않은 문제였다.