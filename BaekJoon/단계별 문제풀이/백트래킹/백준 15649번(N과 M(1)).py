##함수 선언 부분
def NPM(s):
    if len(s) == M:
        print(' '.join(map(str,s)))

    for i in range(1, N + 1): #1부터 N까지
        if i in s: #이미 i가 있으면  #가지치기
            continue #넘어간다
        s.append(i)
        NPM(s) #탐색
        s.pop() #탈출

##변수 선언 부분
data = []

##메인 함수 부분
if __name__ == "__main__":
    N, M = map(int,input().split())
    NPM(data)



##자료구조 시간에 배웠던 트리를 이용해서 순회하려고 했지만, 그렇게 되면 tree도 구현해야하고, 메모리를
##많이 잡아먹을 것 같아서 포기했다. 구글의 도움을 조금 받아 코드를 써봤다. 백트래킹의 의미를 조금 알 수 있었다.