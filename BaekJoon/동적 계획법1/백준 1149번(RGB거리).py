##함수 선언 부분##


##변수 선언 부분##
cost = []

##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    cost = [[int(x) for x in input().split()]for _ in range(N)]
    for i in range(1,N): #cost의 값을 갱신해주면서 반복해준다.
        cost[i][0] = min(cost[i - 1][1], cost[i - 1][2]) + cost[i][0]
        cost[i][1] = min(cost[i - 1][0], cost[i - 1][2]) + cost[i][1]
        cost[i][2] = min(cost[i - 1][1], cost[i - 1][0]) + cost[i][2]

    print(min(cost[N-1][0],cost[N-1][1],cost[N-1][2]))