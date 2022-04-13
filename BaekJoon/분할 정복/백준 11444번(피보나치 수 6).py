##함수 선언 부분
MAX_NUM = 1000000007
def mult_mat(A, B): #행렬 A와 B의 곱 반환
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += (A[i][k] % MAX_NUM * B[k][j] % MAX_NUM) % MAX_NUM
    return C
def Fibo(A, N):
    if N == 1:
        for i in range(2): #나머지 연산
            for j in range(2):
                A[i][j] = A[i][j] % MAX_NUM
        return A
    else:
        ttmp = Fibo(A, N // 2)
        if N % 2 == 0:
            return mult_mat(ttmp, ttmp)
        else:
            return mult_mat(mult_mat(ttmp,ttmp), A)


##변수 선언 부분
A = [[1, 1], [1, 0]]
B = [[1],[0]]
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    tmp = Fibo(A, N)
    _C = [[0], [0]]
    for i in range(2):
        for j in range(2):
            _C[i][0] += (tmp[i][j] % MAX_NUM * B[j][0] % MAX_NUM) % MAX_NUM
    print(_C[1][0])