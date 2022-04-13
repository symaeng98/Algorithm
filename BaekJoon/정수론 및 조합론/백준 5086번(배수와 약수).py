##함수 선언 부분##


##변수 선언 부분##


##메인 함수 부분##
if __name__ == "__main__":
    while True:
        a,b = map(int,input().split())
        if a == 0 and b == 0:
            break
        if b % a == 0:
            print("factor")
        elif a % b == 0:
            print("multiple")
        else:
            print("neither")