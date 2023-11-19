##함수 선언 부분##
def Plus_calculation(e): #덧셈 식을 계산해주는 함수
    num = []
    sum_num = 0
    length = 0
    for i in range(len(e)): #받은 배열의 길이만큼
        if e[i] != '+': #+가 아닐 때는
            num.append(e[i]) #num에 숫자를 append해주고
        if e[i] == '+' or i == len(e)-1: #+이거나 배열이 끝나면,
            length = len(num)
            for j in range(length):#num의 자릿수만큼
                sum_num += int(num.pop())*(10**j) #num을 pop해주고 10씩 반복해서 자릿수를 맞추어준다.
    return sum_num

##변수 선언 부분##
math = []
isFirst = 0
plus = []
sum = 0
##메인 함수 부분##
if __name__ == "__main__":
    math = input()
    for i in range(len(math)):
        if math[i] != '-': #-가 아니면 식을 append
            plus.append(math[i])
        if math[i] == '-' or i == len(math)-1: #-거나 식의 끝일 때,
            if isFirst == 0: #첫번째 시행이면,
                sum += Plus_calculation(plus) #더해주고
                isFirst = 1
            else: #두번째 이상 시행부터는
                sum -= Plus_calculation(plus) #-인 경우이기 때문에, 값을 빼준다.
            del(plus) #배열 초기화
            plus = []

    print(sum)