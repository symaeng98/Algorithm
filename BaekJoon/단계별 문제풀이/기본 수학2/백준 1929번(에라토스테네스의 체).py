##함수 선언 부분##


##변수 선언 부분##
M = 0
N = 0
##메인 함수 부분##
if __name__ == "__main__":
    M, N = map(int,input().split())
    prime = (N+1) * [True] #N+1개의 1차원 배열을 만들어서 하나하나 삭제해줄 예정이다.
    prime[1] = False #1은 소수가 아니므로 표시해준다.
    for i in range(2,N+1): #2부터 차례대로 배수를 지운다
        if prime[i]: #True면
            for j in range(i*2,N+1,i): #본인을 제외한 배수대로 False를 넣어준다.
                prime[j] = False

    for i in range(M, N+1):
        if prime[i]:
            print(i)


##처음에는 그냥 쉽게 변형한 문제구나 했지만, 새로운 알고리즘을 써야했다.
##이 알고리즘을 사용하면 O(n)에서 O(n^1/2)로 크게 줄일 수 있다.
