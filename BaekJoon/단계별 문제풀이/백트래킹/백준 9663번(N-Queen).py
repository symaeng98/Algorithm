##함수 선언 부분
def Queen(index):
    global cnt_Queen
    if index == N:
        cnt_Queen += 1
        return
    for col in range(N):
        if row[col] + left[index + col] + right[index - col + N - 1] == 0:
            row[col] = left[index + col] = right[index - col + N - 1] = 1 #퀸 넣어줌
            Queen(index + 1)
            row[col] = left[index + col] = right[index - col + N - 1] = 0 #퀸 빼줌


##변수 선언 부분
data = []
cnt_Queen = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    row, left, right = [0 for _ in range(N)], [0 for _ in range(2*N-1)], [0 for _ in range(2*N - 1)]
    Queen(0)
    print(cnt_Queen)

##처음 봤을 땐 그렇게 어렵지 않을것 같다고 생각했다. 크기가 1~15까지므로 2차원 배열로 하나하나 옮기면서
##퀸이 놓일 수 있으면 값을 바꿔주고 놓일 수 없는 곳도 값을 설정해줘서 값이 0인 곳만 퀸이 놓일 수 있게
##재귀를 사용해보았지만, 그렇게 되면 함수가 백트래킹하는 과정에서 이전의 값으로 돌아가는 것이 아니라
##새롭게 값을 바꾸는 바람에 이전의 데이터를 저장할 수 없었다. 위 코드는 2차원 배열이 아닌 1차원 배열로
##row와 왼쪽 대각선, 오른쪽 대각선을 구현하고 index를 높이면서 (행을 바꿔가면서) 비교한다.
##행과 열의 합, 차를 이용하는 것은 처음 코드와 같았지만, 값을 모두 바꾸어주는 것이 아닌 퀸이 놓인 위치만
##값을 바꾸어 주었다. 1차원 배열로 2차원을 구현할 수 있다는 것이 신기했다.