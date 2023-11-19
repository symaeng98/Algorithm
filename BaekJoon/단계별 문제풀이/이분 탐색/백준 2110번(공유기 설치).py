##함수 선언 부분

##변수 선언 부분
sh = []
ans = 0
##메인 함수 부분
if __name__ == "__main__":
    N, C = map(int, input().split())
    sh = [int(input()) for _ in range(N)]
    sh.sort()
    left = 1
    right = sh[-1] - sh[0]
    while left <= right:
        mid = (left + right) // 2
        cur = sh[0]
        cnt = 1
        for i in range(1, len(sh)):
            if sh[i] >= mid + cur:
                cnt += 1
                cur = sh[i]
        if cnt < C:
            right = mid - 1
        else:
            left = mid + 1
            ans = mid

    print(ans)