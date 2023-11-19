##함수 선언 부분##
import sys
##변수 선언 부분##
s = []
dp = []
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        s.append(int(input()))
    dp.append(s[0]) #N=1인 경우
    if N == 1:
        print(dp.pop())
        sys.exit(0)
    dp.append(s[0]+s[1]) #N=2인 경우
    if N == 2:
        print(dp.pop())
        sys.exit(0)
    dp.append(max(s[0]+s[2], s[1]+s[2])) #N=3인 경우
    for i in range(3,N): #N>3인 경우
        dp.append(max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i]))
    #마지막 발판을 밟아야하기 때문에, 바로 그 전 발판을 밟은 경우의 최댓값과, 전전 발판을 밟은 경우의 최댓값 중
    #큰 값을 비교해야 된다.
    print(dp.pop())