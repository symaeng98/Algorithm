##함수 선언 부분##
def Fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return Fibo(N-1) + Fibo(N-2)
##변수 선언 부분##
N = 0
##메인 함수 부분##
if __name__ == "__main__" :
    N = int(input("피보나치 수열 F(N)의 N값을 입력하세요 --> "))
    print("F(%d) = %d"%(N, Fibo(N)))