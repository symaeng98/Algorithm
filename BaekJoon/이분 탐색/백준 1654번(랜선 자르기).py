##함수 선언 부분

##변수 선언 부분
A = []
B = []
LAN = []
##메인 함수 부분
if __name__ == "__main__":
    K, N = map(int, input().split())
    LAN = [int(input()) for _ in range(K)]
    left = 1
    right = max(LAN)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for num in LAN:
            cnt += num // mid
        if N <= cnt: #개수가 많거나 같을 경우
            left = mid + 1
        else: #개수가 적은 경우
            right = mid - 1
    print(right)