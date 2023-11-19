##함수 선언 부분

##변수 선언 부분
Tree = []

##메인 함수 부분
if __name__ == "__main__":
    N, M = map(int, input().split())
    Tree = [int(x) for x in input().split()]
    left = 1
    right = max(Tree)
    while left <= right:
        mid = (left + right) // 2
        length = 0
        for i in Tree:
            if i - mid > 0:
                length += i - mid
            else:
                continue
        if length >= M:
            left = mid + 1
        elif length < M:
            right = mid - 1
            
    print(right)