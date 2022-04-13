##함수 선언 부분##


##변수 선언 부분##
A = []

##메인 함수 부분##
if __name__ == "__main__":
    N_num = int(input())
    A = [int(x) for x in input().split()]
    print(min(A)*max(A))