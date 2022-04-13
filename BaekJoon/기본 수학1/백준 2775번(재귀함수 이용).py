##함수 선언 부분##
def Apartment(k, n):
    room = 0
    if k == 0:  ##0층이면
        return n ##몇호인지 return
    else:
        for j in range(1, n+1):
            room += Apartment(k-1, j) ##그 밑 층으로 이동
        return room

##변수 선언 부분##
T = 0
k = 0
n = 0
ans = 0
##메인 함수 부분##
if __name__ == "__main__" :
    T = int(input())
    for i in range(0, T):
        k = int(input())
        n = int(input())
        ans = Apartment(k, n)
        print(ans)

##백준에서 재귀함수 풀이를 원하지 않나보다.
##시간초과가 나오지만 좀 더 간단하게 코드가 나와서 이렇게도 풀어봤다.