##함수 선언 부분


##변수 선언 부분


##메인 함수 부분
if __name__ == "__main__":
    N, M = map(int,input().split())
    A = [[int(x) for x in input().split()]for y in range(N)]
    M, K = map(int, input().split())
    B = [[int(x) for x in input().split()] for y in range(M)]
    C = [[0]*K for x in range(N)]
    for i in range(N): #3
        for j in range(K): #3
            for k in range(M): #2
                C[i][j] += A[i][k] * B[k][j]
            print(C[i][j],end=" ")
        print("")