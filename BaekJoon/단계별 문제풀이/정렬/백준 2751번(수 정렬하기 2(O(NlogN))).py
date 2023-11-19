##함수 선언 부분



##변수 선언 부분
N = 0
data = []
a = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    for i in range(0, N):
        a = int(input())
        data.append(a)


    data.sort() #파이썬의 기본 라이브러리에 있는 sort()는 시간 복잡도가 O(NlogN)이다

    for i in range(0, N):
        print(data[i])

##이 문제에서는 일단 함수를 한번 써보고 다음 문제부터 알고리즘을 써보자
##python3를 사용하면 시간초과가 뜬다. pypy3를 사용해서 더 빠르게 연산을 하도록 해야한다고한다.