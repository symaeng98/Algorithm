##함수 선언 부분##


##변수 선언 부분##


##메인 함수 부분##
if __name__ == "__main__":
    N, K = map(int,input().split())
    N_sum, K_sum = 1, 1
    for i in range(1,K+1):
        K_sum *= i
        N_sum *= N-i+1
    print((N_sum//K_sum)%10007)