##함수 선언 부분


##변수 선언 부분
N = M = 0
White_First_cnt = 0
Black_First_cnt = 0
min_cnt = 10000
##메인 함수 부분
if __name__ == "__main__":
    N, M = map(int,input().split())
    data = [[x for x in input()]for _ in range(N)] #data 입력

    White_First = [['W' for _ in range(8)]for _ in range(8)]
    Black_First = [['B' for _ in range(8)] for _ in range(8)]
    for i in range(0, 8):
        for j in range(0, 8):
            if i % 2 == 0 and j % 2 == 1:
                White_First[i][j] = 'B'
                Black_First[i][j] = 'W'
            elif i % 2 == 1 and j % 2 == 0:
                White_First[i][j] = 'B'
                Black_First[i][j] = 'W'

    for i in range(0, N - 7): #N - 7번씩 판을 옮겨가면서 횟수를 구한다
        for j in range(0, M - 7):
            White_First_cnt = 0
            Black_First_cnt = 0
            for k in range(0, 8): #8X8판을 가지고 비교
                for l in range(0, 8):
                    if data[i+k][j+l] != White_First[k][l]: #
                        White_First_cnt += 1
                    if data[i+k][j+l] != Black_First[k][l]:
                        Black_First_cnt += 1

            if min_cnt > White_First_cnt: #최소 시행을 구해준다.
                min_cnt = White_First_cnt
            if min_cnt > Black_First_cnt:
                min_cnt = Black_First_cnt

    print(min_cnt)


##군대에서 풀었을 때는 어려워서 구글링해보고 풀었던 것 같은데, 생각보다 그렇게 어렵지는 않았다.
##실력이 늘은건지 아니면 두번째 풀어서 그런건지 잘 모르겠지만 이번 문제에서도 문자열 입력방법을 배웠다.