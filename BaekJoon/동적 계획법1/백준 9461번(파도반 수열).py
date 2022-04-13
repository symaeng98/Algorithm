##함수 선언 부분##


##변수 선언 부분##
p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

##메인 함수 부분##
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        for j in range(11,N+1):
            tmp = p[j-5] + p[j-1] #문제의 점화식
            p.append(tmp)
        print(p[N])
        for j in range(N - 10): #반드시 초기화를 해줘야한다.
            p.pop()
