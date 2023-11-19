##함수 선언 부분


##변수 선언 부분
ans = []
queue = []
cnt = 0
p = 0
##메인 함수 부분
if __name__ == "__main__":
    N, K = map(int, input().split())
    for i in range(1,N+1):
        queue.append(i)
    while True:
        if len(ans) == N: #모든 값을 제거했으면
            print("<",end="")
            for i in range(len(ans)-1):
                print("%d, "%(ans[i]),end="")
            print("%d>"%ans[N-1])
            break #출력 후 반복문 탈출
        if queue[p] != 0: #큐를 순회하는 p가 가리키는 값이 0이 아니면,
            cnt += 1 #cnt 증가
            if cnt == K: #cnt가 K면
                cnt = 0 #cnt는 초기화되고
                ans.append(queue[p]) #ans값에 제거할 값을 넣어주고
                queue[p] = 0 #제거해준다.
            p = (p + 1) % N #순회
        else: #값이 0이면 계속 순회
            p = (p + 1) % N