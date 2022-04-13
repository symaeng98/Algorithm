##함수 선언 부분
def divide_square(square, start, end):
    if start == end:
        return square[start]
    else:
        mid = (start + end) // 2
        cnt = 2 #너비를 의미한다
        left = mid #경계 왼쪽
        right = mid+1 #경계 오른쪽
        min_tmp = min(square[left], square[right]) #둘 중에 작은 값을 min_tmp에 넣어준다.
        tmp = min_tmp * 2 #너비에 min_tmp를 곱한 값이 경계를 사이에 두고 정해지는 직사각형의 크기
        while True:
            if (square[left] == 0 or left == start) and (square[right] == 0 or right == end):
                #(왼쪽 경계의 값이 0이거나 더 이상 왼쪽으로 이동할 수 없고) (오른쪽 경계의 값이 0이거나 더 이상 오른쪽으로 이동할 수 없는 경우)
                #반복문 탈출
                break
            elif square[left] == 0 or left == start: #왼쪽 경계의 값이 0 이거나 제일 왼쪽으로 모두 이동한 경우
                if square[right + 1] < min_tmp: #경계 오른쪽으로 이동하는데, 만약 min_tmp보다 값이 작아야 갱신해준다.
                    min_tmp = square[right + 1]
                right += 1
            elif square[right] == 0 or right == end: #위의 경우와 반대로 이미 제일 오른쪽으로 모두 이동한 경우
                if square[left - 1] < min_tmp:
                    min_tmp = square[left - 1]
                left -= 1
            else: #왼쪽 혹은 오른쪽으로 모두 이동할 수 있는 경우
                if square[left - 1] > square[right + 1]: #왼쪽으로 이동시의 값이 더 크면
                    if square[left - 1] < min_tmp: #위와 마찬가지로 min_tmp보다 작은 경우만 갱신해준다.
                        min_tmp = square[left - 1]
                    left -= 1
                else:
                    if square[right + 1] < min_tmp:
                        min_tmp = square[right + 1]
                    right += 1
            cnt += 1 #이동할 때마다 너비 1 증가

            tmp = max(tmp, min_tmp * cnt) #이전의 tmp와 min_tmp에 너비를 곱한 값 중에 큰 값을 tmp에 저장해준다.
        return max(divide_square(square, start, mid), divide_square(square, mid+1, end), tmp)

##변수 선언 부분
histo = []

##메인 함수 부분
if __name__ == "__main__":
    while True:
        histo = list(map(int, input().split()))
        if histo[0] == 0:
            break
        print(divide_square(histo, 1, len(histo)-1))