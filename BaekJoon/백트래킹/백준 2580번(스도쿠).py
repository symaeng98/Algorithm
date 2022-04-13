##함수 선언 부분
import sys

def SDK(index):
    if index == len(zero):
        for i in range(9):
            for j in range(9):
                print("%d" % (sudoku[i][j]), end=" ")
            print()
        sys.exit(0)

    else:
        for k in range(1, 10): #1~9까지 숫자를 넣어주면서 다르면 다시 0을 넣어준다.
            x, y = zero[index]
            if isRight(x, y, k):
                sudoku[x][y] = k
                SDK(index+1)
                sudoku[x][y] = 0


def isRight(x,y,k):
    for i in range(9):
        if k in sudoku[x]: #이미 가로줄에 그 숫자가 있거나
            return False
        elif sudoku[i][y] == k: #세로줄에 있으면
            return False #False 반환해준다

    for i in range(3):
        for j in range(3):
            if sudoku[x // 3 * 3 + i][y // 3 * 3 + j] == k: #3X3 사각형의 좌측 상단의 인덱스 이용해서 탐색하면서 판단
                return False #있으면 False반환

    return True #둘다 없으면 True 반환



##변수 선언 부분
sudoku = []

##메인 함수 부분
if __name__ == "__main__":
    sudoku = [[int(x) for x in input().split()]for _ in range(9)]
    zero = [[i, j] for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    SDK(0)

##입력 예시는 잘 출력 됐지만 다른 곳에서 오류가 있었던 것 같다. 백트래킹 문제를 풀 때 마다 정답을
##보면 꼭 넣어주고 -> 재귀 해주고 -> 빼주는 식인 것 같다. 어떻게 하면 이 논리로 풀 지를 생각해야
##문제를 풀 수 있을 것 같다. 또한 출력 후에 return을 해주는 것이 아닌 sys.exit(0)을 사용하여
##시스템을 아예 종료해야 된다.
