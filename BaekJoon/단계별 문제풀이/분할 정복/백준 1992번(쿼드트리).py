##함수 선언 부분
def get_paper(square, left1, left2, right1, right2):
    is_one = 1
    is_zero = 1
    for i in range(left1, right1+1): #범위 안의 사각형이 모두 1인가 확인
        for j in range(left2, right2+1):
            if square[i][j] == 1:
                is_one = 1
            else:
                is_one = 0
                break
        if not is_one:
            break
    if is_one:
        print(1,end="")
        return

    for i in range(left1, right1+1): #범위 안의 사각형이 모두 0인가 확인
        for j in range(left2, right2+1):
            if square[i][j] == 0:
                is_zero = 1
            else:
                is_zero = 0
                break
        if not is_zero:
            break
    if is_zero:
        print(0,end="")
        return

    if left1 < right1 and left2 < right2 : #
        mid1 = (left1 + right1)//2
        mid2 = (left2 + right2)//2
        print("(",end="")
        get_paper(square, left1,left2,mid1,mid2)
        get_paper(square, left1, mid2+1, mid1, right2)
        get_paper(square, mid1+1, left2, right1, mid2)
        get_paper(square, mid1+1, mid2+1, right1, right2)
        print(")", end="")
##변수 선언 부분
square = []

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    square = [list(map(int,input()))for y in range(N)]
    get_paper(square, 0, 0, N-1, N-1)