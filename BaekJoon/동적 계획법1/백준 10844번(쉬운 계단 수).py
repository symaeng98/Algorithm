##함수 선언 부분##


##변수 선언 부분##
div_num = 10**9
data = []
sum = 0
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    data = [[0]*10 for x in range(N+1)]
    for i in range(1,10): #자리수가 1일 때는 1~9까지는 1로 초기화
        data[1][i] = 1

    for i in range(2,N+1): #1~N자리수까지
        data[i][0] = data[i-1][1] #0으로 끝나는 경우의 바로 전 시행은 1이다
        for j in range(1, 9): #1~8까지는 각각 두가지 경우가 있다
            data[i][j] = data[i-1][j-1] + data[i-1][j+1]
        data[i][9] = data[i-1][8] #9로 끝나는 경우의 바로 전 시행은 8이다

    for i in range(0,10):
        sum += data[N][i] #각 값들마다의 합을 구한다.

    print(sum%div_num)

