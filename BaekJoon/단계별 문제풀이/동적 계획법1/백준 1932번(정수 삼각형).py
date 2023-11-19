##함수 선언 부분##

##변수 선언 부분##
t = []

##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    t = [[int(x) for x in input().split()]for y in range(N)]
    for i in range(N-1,0,-1): #N-1번째부터 위로 올라가면서 진행
        for j in range(i): #i번 만큼 max를 구해준다.
            t[i-1][j] = max(t[i][j],t[i][j+1]) + t[i-1][j]

    print(t[0][0])