n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(board[j][i])
    board.append(tmp)


result = 0
def solution(arr):
    valid = [True]*n
    for i in range(1, n):
        if abs(arr[i]-arr[i-1]) > 1:
            return False
        if arr[i-1] > arr[i]:
            for j in range(l):
                if i+j >= n:
                    return False
                if arr[i+j] != arr[i]:
                    return False
                if not valid[i+j]:
                    return False
                if valid[i+j]:
                    valid[i+j] = False
        elif arr[i-1] < arr[i]:
            for j in range(l):
                if i-j-1 < 0:
                    return False
                if arr[i-j-1] != arr[i-1]:
                    return False
                if not valid[i-j-1]:
                    return False
                if valid[i-j-1]:
                    valid[i-j-1] = False

    return True


for b in board:
    if solution(b):
        result += 1


print(result)