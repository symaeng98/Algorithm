##함수 선언 부분
import sys


##변수 선언 부분
data = []

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    data = [[int(x) for x in input().split()]for _ in range(N)]
    # data.sort()
    # print(data)
    # data.sort(key = lambda x : (x[0], -x[1]))
    # print(data) #파이썬으로 2차원 배열을 마음대로 정렬하는 법
    data.sort(key = lambda x : (x[1],x[0])) #x[1] -> j 오름차순 정렬 후 x[0] -> i 오름차순 정렬
    for i in range(N):
        for j in range(2):
            print(data[i][j],end=" ")
        print("")


##파이썬에서 sort()는 그냥 i 오름차순 후 j 오름차순 고정이 아닌 직접 어떤 방식으로 정렬할 지 결정할 수 있다.
##lamda 함수를 사용하는 법에 대해 배웠다. 이름 없는 함수 정도로 알고 있으면 될 것 같다. sort()에서 key로 많이 사용한다는 정도

