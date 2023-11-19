##함수 선언 부분
import sys
input = sys.stdin.readline
##변수 선언 부분
A = []
dp = [0]
mid = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    A = [int(x) for x in input().split()]
    for i in range(N):
        left = 1
        right = len(dp) - 1
        if dp[-1] < A[i]:
            dp.append(A[i])
        else:
            while left <= right:
                mid = (left + right) // 2
                if A[i] < dp[mid]:
                    right = mid - 1
                elif A[i] > dp[mid]:
                    left = mid + 1
                else: #같은 경우는 통과
                    mid = -1
                    break
            if mid == -1: #통과
                continue
            else:
                dp[left] = A[i]
    print(len(dp)-1)