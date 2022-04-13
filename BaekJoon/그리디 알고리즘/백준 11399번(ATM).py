##함수 선언 부분##


##변수 선언 부분##
atm = []
sum = 0
sum1 = 0
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    atm = [int(x) for x in input().split()]
    atm.sort()
    for i in range(N):
        sum = sum + atm[i]
        sum1 += sum

    print(sum1)