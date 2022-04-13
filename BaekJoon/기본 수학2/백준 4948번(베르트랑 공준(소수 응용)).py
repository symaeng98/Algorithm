##함수 선언 부분


##변수 선언 부분
isPrime = 0
cnt = 0
prime = []
##메인 함수 부분
if __name__ == "__main__":
    prime = 250000 * [True] #250000개의 True가 들어있는 배열을 만들어준다.
    for i in range(2,500): #250000의 제곱근만큼 반복해줘도 된다
        for j in range(2*i,250000,i): #본인의 배수들을 모두 지워준다.
            if prime[j]:
                prime[j] = False

    while True:
        cnt = 0
        T = int(input())
        if T == 0: #0이 입력되면 종료
            break
        for i in range(T+1,T*2+1): #본인 + 1 ~ 본인 * 2까지
            if prime[i] == True: #소수면 cnt 증가
                cnt += 1

        print(cnt)


##에라토스테네스의 체를 이용해서 베르트랑 공준을 배웠다. n보다 크고 2n보다 작거나 같은 소수는
##적어도 하나 존재한다는 내용이다. 25만개의 배열을 선언해서 풀어서 딱히 좋은 문제는 아닌 것 같다.

