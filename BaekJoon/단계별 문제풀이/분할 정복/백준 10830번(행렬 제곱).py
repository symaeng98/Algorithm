##함수 선언 부분
def mat_mult(A, B, N):
    C = [[0]*N for x in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
    for i in range(N):
        for j in range(N):
            C[i][j] = C[i][j] % 1000
    return C
def mult(A, B, N):
    if B == 1:
        for i in range(N): #나머지값 저장
            for j in range(N):
                A[i][j] = A[i][j] % 1000
        return A

    if B % 2 == 0:
        tmp = mult(A, B // 2, N)
        C = mat_mult(tmp,tmp,N)
        return C
    else:
        tmp = mult(A, B-1, N)
        C = mat_mult(tmp,A,N)
        return C

##변수 선언 부분


##메인 함수 부분
if __name__ == "__main__":
    N, B = map(int,input().split())
    A = [[int(x) for x in input().split()]for y in range(N)]
    ans = mult(A,B,N)
    for i in range(N):
        for j in range(N):
            print(ans[i][j],end=" ")
        print("")