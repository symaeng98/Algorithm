##함수 선언 부분

##변수 선언 부분
ans = 0

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    k = int(input())
    left = 1
    right = N ** 2
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)
        cnt = 0
        for i in range(1, N+1): #1,1부터 N,N까지 조건에 맞는 것을 세준다
            if mid // i > N: #찾으려는 수를 i로 나누어주면 개수가 나온다.
                cnt += N #최대 개수가 N이기 때문에 N을 넘으면 N을 더해준다.
            else: #N보다 작으면
                cnt += mid // i #i로 나눈 값을 더한다.
        print(cnt)
        if cnt >= k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)