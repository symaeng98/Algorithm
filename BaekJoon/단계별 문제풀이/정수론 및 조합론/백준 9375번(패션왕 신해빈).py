##함수 선언 부분##


##변수 선언 부분##


##메인 함수 부분##
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        kinds_name = [] #의상의 종류의 이름
        kinds_num = [] #의상의 종류의 개수
        isEmpty = 1 #의상의 종류가 이전에 있었는 지 확인
        sum = 1 #경우의 수
        N = int(input())
        for j in range(N):
            name, kinds = input().split() #의상의 이름과 의상의 종류 입력
            for k in range(len(kinds_name)): #종류가 이미 있는 종류인지 확인
                if kinds == kinds_name[k]: #이미 있으면,
                    kinds_num[k] += 1 #개수 하나 증가
                    isEmpty = 0 #이미 있는 종류임을 확인
                    break
                isEmpty = 1 #없는 종류
            if isEmpty: #새로운 종류면
                kinds_name.append(kinds) #추가
                kinds_num.append(1) #개수도 1로 추가

        for j in range(len(kinds_name)):
            sum *= kinds_num[j]+1
        print(sum-1)

        del(kinds_num)
        del(kinds_name)

