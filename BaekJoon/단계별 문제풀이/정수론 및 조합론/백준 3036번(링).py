##함수 선언 부분##
from math import gcd

##변수 선언 부분##
ring = []
a, b = 0, 0
GCD = 0
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    ring = [int(x) for x in input().split()]
    for i in range(1,N):
        GCD = gcd(ring[0], ring[i]) #최대공약수를 구해준다.
        a = ring[0] // GCD #각 값을 최대공약수로 나누어준다.
        b = ring[i] // GCD
        print("%d/%d"%(a,b))