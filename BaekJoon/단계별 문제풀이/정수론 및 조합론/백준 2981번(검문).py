##함수 선언 부분##
from math import gcd

##변수 선언 부분##
A = []
B = []
min = 0
min_i = 0
tmp = 0
divisor = []
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        A.append(int(input()))

    A.sort() #차를 구하기 위해 정렬
    for i in range(1,N):
        B.append(A[i]-A[i-1]) #차를 구해줌

    tmp = B[0]
    for i in range(1,len(B)):
        tmp = gcd(tmp,B[i]) #처음부터 마지막까지 gcd를 갱신하며 반복문 순회
    for i in range(2, int(tmp**0.5)+1): #약수를 구할 때 자기자신까지 반복문을 돌리면 시간초과
        if tmp % i == 0:
            divisor.append(i)
            divisor.append(tmp//i)

    divisor.append(tmp) #자기자신도 append
    divisor = list(set(divisor)) #중복 값을 제거하기 위해 set로 변환했다가 다시 list로 변환
    divisor.sort() #오름차순 정렬
    print(*divisor)