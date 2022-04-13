##함수 선언 부분##

##변수 선언 부분##
Str = []
cnt = 0
##메인 함수 부분##
if __name__ == "__main__" :
    Str = input()
    for i in range(0,len(Str)):
        if(Str[i]>='A' and Str[i]<='C'): ##해당하는 알파벳의 거리만큼 더해준다
            cnt+=3
        elif(Str[i]>='D' and Str[i]<='F'):
            cnt+=4
        elif (Str[i] >= 'G' and Str[i] <= 'I'):
            cnt += 5
        elif (Str[i] >= 'J' and Str[i] <= 'L'):
            cnt += 6
        elif (Str[i] >= 'M' and Str[i] <= 'O'):
            cnt += 7
        elif (Str[i] >= 'P' and Str[i] <= 'S'):
            cnt += 8
        elif (Str[i] >= 'T' and Str[i] <= 'V'):
            cnt += 9
        else:
            cnt += 10

    print("%d"%cnt)

##해당하는 알파벳만큼 cnt를 더해서 올려주면 되는 문제
##쉽게 풀 수 있다.