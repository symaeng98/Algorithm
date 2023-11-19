##함수 선언 부분##


##변수 선언 부분##


##메인 함수 부분##
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, M = map(int,input().split())
        M_sum, N_sum = 1, 1
        for i in range(1, N+1):
            N_sum *= i
            M_sum *= M-i+1
        print(M_sum//N_sum)

##다리를 놓는 경우를 생각을 해보면 M중에서 N개만큼 임의로 선택을 해주고 그것을 위에부터 N개의 다리에
##연결해주면 되기 때문에 Combination의 값과 같다.