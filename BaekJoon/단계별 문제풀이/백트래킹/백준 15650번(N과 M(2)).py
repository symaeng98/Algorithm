##함수 선언 부분
def P(s):
    if len(s) == M:
        for i in range(0, M-1): #오름차순이 아니면 return해줘야 한다
            if s[i] > s[i+1]: #바로 다음 수와 비교해서 더 크면
                return #탈출
        print(' '.join(map(str,s)))
        return

    for i in range(1, N+1):
        if i in s:
            continue
        s.append(i)
        P(s)
        s.pop()

##변수 선언 부분
data = []

##메인 함수 부분
if __name__ == "__main__":
    N, M = map(int,input().split())
    P(data)

##15649번을 풀었으면 어렵지 않은 문제였다. 조건만 하나 넣어주면 된다.