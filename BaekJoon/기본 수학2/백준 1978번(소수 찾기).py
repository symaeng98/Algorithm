##함수 선언 부분##

##변수 선언 부분##
N = 0
arr = []
isRight = 0
cnt = 0
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    arr = [int(x) for x in input().split()]
    for i in arr:
        isRight = 0
        for j in range(2, i):
            if i % j == 0:
                isRight = 0
                break
            isRight = 1
        if isRight == 1 or i == 2:
            cnt += 1

    print(cnt)


## 2가 소수가 아닌줄 알고 코드의 다른 부분에서 오류를 찾았다.