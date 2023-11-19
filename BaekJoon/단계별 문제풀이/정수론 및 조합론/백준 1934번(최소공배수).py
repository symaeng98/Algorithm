##함수 선언 부분##


##변수 선언 부분##


##메인 함수 부분##
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        A, B = map(int,input().split())
        j = 1
        while True:
            if (max(A, B)*j)%min(A,B) == 0:
                print(max(A,B)*j)
                break
            else:
                j += 1