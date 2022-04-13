##함수 선언 부분
def get_paper(square, left1, left2, size, answer):
    is_one = 1
    is_zero = 1
    is_minus_one = 1
    for i in range(size): #범위 안의 사각형이 모두 1인가 확인
        for j in range(size):
            if square[left1+i][left2+j] == 1:
                is_one = 1
            else:
                is_one = 0
                break
        if not is_one:
            break
    if is_one:
        answer[1] += 1
        return

    for i in range(size):  # 범위 안의 사각형이 모두 0인가 확인
        for j in range(size):
            if square[left1 + i][left2 + j] == 0:
                is_zero = 1
            else:
                is_zero = 0
                break
        if not is_zero:
            break
    if is_zero:
        answer[0] += 1
        return

    for i in range(size): #범위 안의 사각형이 모두 -1인가 확인
        for j in range(size):
            if square[left1+i][left2+j] == -1:
                is_minus_one = 1
            else:
                is_minus_one = 0
                break
        if not is_minus_one:
            break
    if is_minus_one:
        answer[-1] += 1
        return

    if size >= 1:
        size//=3
        get_paper(square, left1, left2, size, answer)
        get_paper(square, left1, left2 + size, size, answer)
        get_paper(square, left1, left2 + size * 2, size, answer)
        get_paper(square, left1 + size, left2, size, answer)
        get_paper(square, left1 + size, left2 + size, size, answer)
        get_paper(square, left1 + size, left2 + size * 2, size, answer)
        get_paper(square, left1 + size * 2, left2, size, answer)
        get_paper(square, left1 + size * 2, left2 + size, size, answer)
        get_paper(square, left1 + size * 2, left2 + size * 2, size, answer)
##변수 선언 부분
square = []

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    square = [[int(x) for x in input().split()]for y in range(N)]
    answer = [0]*3
    get_paper(square, 0, 0, N, answer)
    print(answer[-1])
    print(answer[0])
    print(answer[1])