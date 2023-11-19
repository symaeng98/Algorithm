##함수 선언 부분
def mult(a,b):
    if b == 1:
        return a % p
    tmp = mult(a,b//2)
    if b % 2 != 0:
        return ((tmp ** 2) * a) % p
    else:
        return (tmp ** 2) % p

##변수 선언 부분
p = 1000000007
fact = [1]*40000002
##메인 함수 부분
if __name__ == "__main__":
    N, K = map(int, input().split())
    #A = n!, B = K!(n-k)!
    for i in range(2,N+1):
        fact[i] = (fact[i-1] * i) % p
    A = fact[N]; B = fact[K] * fact[N-K]
    B_P_2 = mult(B,p-2)
    print((A%p * B_P_2%p)%p)