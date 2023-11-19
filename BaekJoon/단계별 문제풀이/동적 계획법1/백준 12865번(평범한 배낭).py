##함수 선언 부분##


##변수 선언 부분##
dp = []
stuff = []
value = []
max_sum = []
##메인 함수 부분##
if __name__ == "__main__":
    N, K = map(int, input().split())
    for i in range(N):
        s, v = map(int, input().split())
        stuff.append(s)
        value.append(v)
    max_sum = [[0]*(K+1) for x in range(N)]

    for i in range(K+1): #max_sum의 첫번째 값 설정
        if i - stuff[0] < 0:
            max_sum[0][i] = 0
        else:
            max_sum[0][i] = value[0]

    for i in range(1,N):
        for j in range(K+1):
            if j - stuff[i] < 0: #가방에 들어갈 자리가 없으면
                max_sum[i][j] = max_sum[i - 1][j] #값 갱신
            else: #들어갈 자리가 있고
                if max_sum[i-1][j] < (value[i]+max_sum[i-1][j-stuff[i]]): #이전 배열에서, 현재 탐색하는 수와 K의 차이만큼일 때 최대 이윤 값과 비교
                    max_sum[i][j] = value[i]+max_sum[i-1][j-stuff[i]]
                else:
                    max_sum[i][j] = max_sum[i-1][j]


    print(max_sum[-1][-1])