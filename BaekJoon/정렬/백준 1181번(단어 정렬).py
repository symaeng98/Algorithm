##함수 선언 부분
import sys


##변수 선언 부분
data = []

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        data.append(input())
    data.sort(key = lambda x : (len(x),x)) #길이 순으로 정렬한 뒤 길이도 같다면 원래 기본 순서대로 정렬
    for i in range(0, N):
        if i == 0:
            print(data[i],end="")
            print("")
        elif data[i] != data[i-1]:
            print(data[i],end="")
            print("")

##key를 변경해서 정렬하는 법을 연습했다. 파이썬이 이래서 좋은건가 싶다. c에서는 아직 배우는 단계이다보니
##함수를 매번 만들어서 사용했어야했는데 파이썬에서는 매소드가 너무 잘 만들어져있는 것 같다.