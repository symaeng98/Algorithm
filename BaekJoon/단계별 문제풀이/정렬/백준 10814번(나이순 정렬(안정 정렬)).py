##함수 선언 부분
import sys


##변수 선언 부분
data = []

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        age, name = map(str, input().split())
        age = int(age)
        data.append((age, name))
    data.sort(key = lambda x: x[0]) #나이순으로만 정렬 나머지는 그대로
    for i in data:
        print(i[0], i[1])

##처음에 썼던 코드가 틀린 이유를 잘 모르겠다. 입출력 방식만 바꿨는데 맞게 나왔다.
##stable sort에 대해 배울 수 있었다. 여러가지 면에서 merge sort가 제일 좋은 방식인 듯 하다. 상황에 따라 다르겠지만..