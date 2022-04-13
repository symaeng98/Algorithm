##함수 선언 부분


##변수 선언 부분


##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    data = [[int(x) for x in input().split()]for y in range(N)] #데이터 입력
    rank = [1] * N
    for i in range(0, N):
        for j in range(0, N):
            if (data[i][0] < data[j][0]) and (data[i][1] < data[j][1]): #키 몸무게 모두 크면
                rank[i] += 1

    for i in rank:
        print(i, end=" ")

##쉬운 문제였지만 2차원 리스트 입력 방법과 출력에 대해 배울 수 있었다.