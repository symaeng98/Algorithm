##함수 선언 부분
import sys


##변수 선언 부분
data = []

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    data = [[int(x) for x in input().split()]for _ in range(N)]
    data.sort()
    for i in range(N):
        for j in range(2):
            print(data[i][j],end=" ")
        print("")

##파이썬의 기본 라이브러리에 있는 sort()는 2차원 리스트를 정렬할 때 i값, j값 순서로 오름차순으로 정렬해준다.