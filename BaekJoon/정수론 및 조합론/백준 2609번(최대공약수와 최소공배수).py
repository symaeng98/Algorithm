##함수 선언 부분##


##변수 선언 부분##
max = 1
##메인 함수 부분##
if __name__ == "__main__":
    A, B = map(int, input().split())
    A_safe, B_safe = A, B
    i = 2
    while True:
        if (i == min(A, B)+1) or (A_safe == 1) or (B_safe == 1):
            break
        if A_safe % i == 0 and B_safe % i == 0:
            A_safe //= i
            B_safe //= i
            max *= i
        else:
            i += 1
    print(max)
    print(A*B//max)