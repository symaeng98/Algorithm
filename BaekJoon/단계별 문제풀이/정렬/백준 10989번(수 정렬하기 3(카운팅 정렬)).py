##함수 선언 부분
import sys


##변수 선언 부분
N = 0
data = []
a = 0
count = []
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    count = [0] * 10001 #count리스트를 만들어 준다.
    for i in range(N):
        a = int(sys.stdin.readline())
        count[a] += 1 #각 값을 카운팅해서 저장해준다.

    for i in range(10001):
        if count[i] != 0:
            for j in range(count[i]):
                print(i)
#N개의 리스트를 만들어 줘서 메모리 초과가 계속 떴었다. 카운팅 소트의 특징을 제대로 이해하지 못했다.
#각 수들의 크기가 그렇게 크지 않을 때 사용해야한다.






