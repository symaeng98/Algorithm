##함수 선언 부분##

##변수 선언 부분##
a = 0
b = 0
N = 0
Min = 10000
flag = 0
##메인 함수 부분##
if __name__ == "__main__" :
    N = int(input())
    for a in range(0, (N//5) + 1):  ##5a + 3b = N에 a를 0부터 대입
        if (N - 5*a) % 3 == 0:
            flag = 1
            b = (N - 5 * a)//3
            if Min > a+b:   ##합이 더 작으면 Min대체해준다
                Min = a+b

    if flag == 0: ##딱 떨어지는 값이 없으면 -1
        print(-1)
    else:
        print(Min)

##5a + 3b = N 이라는 식을 쓰지 않았으면 산으로 갔을 것 같은 문제다.
##하나씩 넣어보면서 최솟값을 찾는 문제