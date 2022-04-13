##함수 선언 부분
def P(s):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return

    for i in range(1, N+1): #if i in s: 조건만 없애주면 된다.
        s.append(i)
        P(s)
        s.pop()

##변수 선언 부분
data = []

##메인 함수 부분
if __name__ == "__main__":
    N, M = map(int,input().split())
    P(data)


##조건 하나만 없애주면 된다.