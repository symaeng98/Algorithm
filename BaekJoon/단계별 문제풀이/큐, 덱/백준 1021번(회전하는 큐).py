##함수 선언 부분

##변수 선언 부분
index = []
circular_dequeue = []
cnt = 0
N_safe = 0
front = 1
sum = 0
##메인 함수 부분
if __name__ == "__main__":
    N, M = map(int,input().split())
    N_safe = N
    index = [int(x) for x in input().split()]
    circular_dequeue = [int(x) for x in range(1,N+1)]
    for i in range(len(index)):
        while front != index[i]: #pop해주려는 index를 찾을 때 까지 오른쪽으로 이동
            if circular_dequeue[front-1] != 0: #pop되지 않은 수만 cnt해준다.
                cnt += 1
            front = (front + 1) % (N+1)
            if front == 0: #front는 1부터 N까지 이므로 0일때는 1로 넘김
                front = 1
        if cnt > N_safe - cnt: #cnt에 더 작은 값을 저장
            cnt = N_safe - cnt
        N_safe -= 1 #원소 개수 하나 줄어듦
        circular_dequeue[front-1] = 0 #pop
        while circular_dequeue[front-1] == 0 and N_safe != 0:
            front = (front + 1) % (N+1) #pop해준 뒤 front 이동
            if front == 0:
                front = 1
        sum += cnt
        cnt = 0
    print(sum)
