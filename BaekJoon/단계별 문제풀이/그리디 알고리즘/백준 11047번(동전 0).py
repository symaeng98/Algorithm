##함수 선언 부분##


##변수 선언 부분##
coin = []
sum = 0
cnt = 0
##메인 함수 부분##
if __name__ == "__main__":
    N, K = map(int,input().split())
    for i in range(N):
        tmp = int(input())
        coin.append(tmp)

    for i in range(N): #사용할 수 있는 동전의 최댓값의 index를 구한다
        if coin[i] > K:
            i = i-1
            break
    for j in range(i,-1,-1): #구한 인덱스부터 거꾸로 반복
        if K == 0:
            break
        tmp = K // coin[j] #몫을 구한다
        if tmp == 0: #나누어지지 않으면 건너뛴다.
            continue
        K -= coin[j] * tmp #K값 갱신
        cnt += tmp
    print(cnt)