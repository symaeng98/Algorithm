##함수 선언 부분##


##변수 선언 부분##


##메인 함수 부분##
if __name__ == "__main__":
    T = int(input()) #테스트 케이스
    for i in range(T):
        fibo = []
        fibo.append(0)
        fibo.append(1)
        N = int(input())
        j = 2 #j는 2부터 원하는 값을 구할 때까지 1씩 증가한다.
        if N == 0:
            print(' '.join(['1','0']))
        elif N == 1:
            print(' '.join(['0','1']))
        else:
            while True:
                if j == N+1:
                    break
                fibo.append(fibo[j-1] + fibo[j-2])
                j += 1
            print(' '.join([str(fibo[N-1]), str(fibo[N])]))
            del(fibo)