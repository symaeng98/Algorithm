##함수 선언 부분##


##변수 선언 부분##
A = []
dp_up = []
dp_down = []
dp_max = []
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    A = [int(x) for x in input().split()]
    dp_up = [1 for x in range(N)] #증가하는 부분 수열을 구하기 위한 dp
    dp_down = [1 for x in range(N)] #감소하는 부분 수열을 구하기 위한 dp
    for i in range(N): #증가하는 부분 수열 구하기
        for j in range(i):
            if A[i] > A[j]: #이전 값이 자신보다 더 작으면
                dp_up[i] = max(dp_up[i], dp_up[j]+1) #이전부터 순회하면서 갱신한 값과 특정 값+1중에 큰 값을 갱신

    for i in range(N-1,-1,-1): #감소하는 부분 수열 구하기
        for j in range(i,N): #N-1부터 시작하면서 거꾸로 구해주면 된다.
            if A[i] > A[j]:
                dp_down[i] = max(dp_down[i],dp_down[j]+1)

    for i in range(N): #두 dp의 각 원소의 합을 dp_max배열에 저장해준다.
        dp_max.append(dp_up[i]+dp_down[i]-1)

    print(max(dp_max))