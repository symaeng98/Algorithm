##함수 선언 부분##
import sys

##변수 선언 부분##
numbers = []

##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    numbers = [-1,0] #N=0, N=1일때 최솟값
    for i in range(2,N+1):
        numbers.append(numbers[i-1]+1) #이전 값에 1을 더한 횟수를 일단 넣어준다.
        if i % 3 == 0: #3으로 나누어 떨어지면,
            numbers[i] = min(numbers[i], numbers[i//3]+1) #이전 값의 정답에 1을 더한 값과 비교
        if i % 2 == 0:
            numbers[i] = min(numbers[i], numbers[i//2]+1)

    print(numbers.pop())