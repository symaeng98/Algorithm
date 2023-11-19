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

    for i in range(N - 1, 0, -1): #N-1번 반복, 첫번째 for문은 그저 반복 횟수만 정해주고
        for j in range(i): #두번째 for문에서 조건을 해결한다.
            if data[j + 1] < data[j]:
                data[j], data[j+1] = data[j+1], data[j] #파이썬에서는 tmp를 써서 변수를 저장해서 바꿔주지 않아도 된다


    for i in range(0, N):
        print(data[i])


##오랜만에 정렬을 써서 그런지 많이 까먹었다. 버블 정렬도 종류가 많은데 그 중 이상한 정렬을 외우고 있어서
##이해하는 데 오래 걸렸다. 기본 정석으로 외워야겠다.