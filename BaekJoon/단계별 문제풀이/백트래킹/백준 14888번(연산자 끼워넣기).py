##함수 선언 부분
def calculator(index, sum):
    global min, max
    if index == N - 1: #연산자가 모두 들어갔으면
        if min > sum:
            min = sum
        if max < sum:
            max = sum

    else:
        for i in range(4): #연산자 4개 탐색
            if cal[i] == 0: #특정 연산자를 다 썼으면
                continue #그대로 진행
            cal[i] -= 1 #연산자 하나를 빼서
            temp = calculate(sum,numbers[index+1],i) #계산을 해주고
            calculator(index+1,temp) #계산한 값을 다시 재귀
            cal[i] += 1 #백트래킹

def calculate(sum, plus, oper): #연산자마다 계산
    if oper == 0:
        return sum + plus
    elif oper == 1:
        return sum - plus
    elif oper == 2:
        return sum * plus
    else:
        if sum < 0:
            sum = -sum // plus
            return -sum
        else:
            return sum // plus

##변수 선언 부분
numbers = []
cal = []
min = 1000000000
max = -1000000000
cnt = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    numbers = [int(x) for x in input().split()] #숫자 입력
    cal = [int(x) for x in input().split()] #+,-,x,// 개수 입력
    calculator(0,numbers[0])
    print(max)
    print(min)
