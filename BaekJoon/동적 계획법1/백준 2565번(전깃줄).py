##함수 선언 부분##


##변수 선언 부분##
data = []
dp = []
LIS = 0
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    data = [[int(x) for x in input().split()]for y in range(N)]
    dp = [1 for x in range(N)]
    data.sort(key=lambda x: x[0]) #첫번째 원소를 기준으로 정렬해준다.

    for i in range(N):
        for j in range(i):
            if data[i][1] > data[j][1]: #두번째 원소들로 이루어진 수열의 LIS를 구한다.
                dp[i] = max(dp[i], dp[j]+1)
    LIS = max(dp)
    print(N-LIS)