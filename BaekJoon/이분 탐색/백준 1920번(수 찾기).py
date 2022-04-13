##함수 선언 부분


##변수 선언 부분
A = []
B = []
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    A = [int(x) for x in input().split()]
    M = int(input())
    B = [int(x) for x in input().split()]
    A.sort()
    for i in range(M):
        left = 0; right = N-1
        while left <= right:
            if right - left == 1:
                if A[right] == B[i] or A[left] == B[i]:
                    print(1)
                    break
                else:
                    print(0)
                    break
            mid = (left + right) // 2
            if A[mid] < B[i]:
                left = mid
            elif A[mid] > B[i]:
                right = mid
            else:
                print(1)
                break