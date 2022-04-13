##함수 선언 부분

##변수 선언 부분
command = []
index_2 = 0
front = 0
isError = 0
##메인 함수 부분
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        isError = 0
        front = 0
        command = input()
        N = int(input())
        number = input()
        number = number.rstrip(']') #괄호와 ,를 포함하여 입력을 받았기 때문에,
        number = number.lstrip('[') #strip과 split을 사용하여 원소만 저장해준다.
        number = number.split(',')
        for j in command:
            if j == 'R': #R명령이면,
                if front == 0: #첫번째 원소를 가리키는 의미인 front에
                    front = -1 #-1을 넣어 마지막 원소를 가리키게한다.
                else: #이미 마지막 원소를 가리키고있다면
                    front = 0 #첫번째 원소를 가리키게한다.
            elif j == 'D': #D명령이면,
                if N == 0: #원소의 개수가 없으면
                    print("error") #error출력
                    isError = 1
                    break #탈출
                number.pop(front) #front가 가리키는 원소를 pop해준다.
                N -= 1 #개수 1개 감소
        if not isError: #error가 아닌 경우에
            print('[',end="")
            if front == -1: #뒤집어 놓은 상태이면
                for j in range(len(number)-1,-1,-1): #거꾸로 출력
                    print(number[j],end="")
                    if j == 0:
                        print(']')
                        break
                    print(',',end="")
            else: #뒤집어 놓은 상태가 아니면,
                print(','.join(number),end="") #그대로 출력
                print(']')
