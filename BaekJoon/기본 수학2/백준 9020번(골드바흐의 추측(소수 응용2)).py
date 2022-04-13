##함수 선언 부분


##변수 선언 부분
T = 0
n = 0
min = 100000
gap = 0
save = 0
##메인 함수 부분
if __name__ == "__main__":
    T = int(input())
    prime = 10001 * [True]
    for i in range(2,101):
        for j in range(2*i,10001,i):
            if prime[j]:
                prime[j] = False
    for _ in range(T):
        n = int(input())
        min = 100000
        gap = 0

        for i in range(2,n): #2부터 반복
            if prime[i] and prime[n-i]: #i와 n에서 i를 뺀 값이 모두 소수면
                if i>n-i: #gap이 -값이 나올 수 있기 때문에 경우를 나눠준다.
                    gap = 2*i - n
                else:
                    gap = n - 2*i
                if(gap<min): #차이가 가장 작은 값을 출력해야하기 때문에
                    min = gap #최솟값을 찾아준다
                    save = i #값 저장
        print('%d %d'%(save,n-save))

##n이 10000까지라 쉬운 방법으로 소수를 구해도 될 줄 알고 썼다가 시간초과가 나와서 고쳤다.
##소수 문제를 풀 때는 앞으로 무조건 아르토스테네스의 체로 풀자