##함수 선언 부분##

##변수 선언 부분##
N = 0
cnt = 0
Str = []
cont = 1
isGroup = 1
flag = 0
##메인 함수 부분##
if __name__ == "__main__" :
    N = int(input())
    for i in range(0, N):
        Str = input()
        isGroup = 1
        flag = 0
        cont = 1
        for j in range(0, len(Str)):
            flag = 0
            cont = 1
            for k in range(0, j):
                if (Str[j] == Str[k]):  ##이전에 이미 훑었던 문자면
                    flag = 1 ##flag로 실행 안하게 넘어가기
                    break

            if(flag == 0): ##훑지 않았다면
                for k in range(j, len(Str)):
                    if(Str[j] == Str[k]): ##뒤에 같은 문자가 나왔다면
                        if(cont == 0): ##연속적이지도 않다면
                            isGroup = 0 ##그룹문자가 아님
                            break
                    else:
                        cont = 0
            if isGroup == 0 : ##그룹문자가 아니라면 break
                break


        if isGroup == 1 : ##그룹문자면 개수 추가
            cnt += 1

    print("%d"%cnt)

##반례 찾느라 시간을 좀 썼던 문제
##어렵지 않게 풀 수 있는데 최대한 메모리를 아껴보자는 의지로 flag까지 넣어서
##2중 반복문을 다 돌리지 않고 앞에서 확인했으면 확인하지 않는 식으로 풀었다.
##변수를 초기화 안해줘서 헤맸던 문제. 조심하자.