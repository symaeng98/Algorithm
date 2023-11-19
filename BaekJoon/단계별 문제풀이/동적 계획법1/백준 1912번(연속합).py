##함수 선언 부분##


##변수 선언 부분##
A = []
dp = []
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    A = [int(x) for x in input().split()]
    dp.append(A[-1]) #A의 마지막 원소부터 차례대로 탐색한다.
    for i in range(N-2, -1, -1):
        dp.append(max((dp[N-i-2]+A[i]), A[i])) #탐색하는 A의 원소와 이전 값에 A의 원소를 더한 값을 비교
    print(max(dp))
