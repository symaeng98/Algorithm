##함수 선언 부분
def P(s):
    if len(s) == M:
        for i in range(0, M-1): #오름차순이 아니면 return해줘야 한다
            if s[i] > s[i+1]: #바로 다음 수와 비교해서 더 크면
                return #탈출
        print(' '.join(map(str,s)))
        return

    for i in range(1, N+1): #if i in s: 조건만 빼주면 된다.
        s.append(i)
        P(s)
        s.pop()

##변수 선언 부분
data = []

##메인 함수 부분
if __name__ == "__main__":
    N, M = map(int,input().split())
    P(data)


##조건 하나만 빼주고 하나 더해주면 된다. N과 M을 풀면서 느낀거지만 좋은 코드는 문제 몇개의 가치가 있는 것 같다.
##N과 M(1)이 제일 중요한 듯 하다. 어떻게 코드가 이렇게 나오고 어떤 사고방식으로 짠건지 잘 보자
