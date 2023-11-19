##함수 선언 부분##

##변수 선언 부분##
A = []
B = []
cnt = 0
sum = 0
List = []
##메인 함수 부분##
if __name__ == "__main__" :
    A, B = input().split()
    if len(A) > len(B):  ##A와 B의 자리수에 따라 코딩을 해줘야한다.
        for i in range(-1,-len(B)-1,-1):  ##짧은 자리수 만큼
            sum = int(A[i]) + int(B[i]) + cnt  ##cnt는 올림수
            cnt = 0
            if sum >= 10:  ##10이 넘으면 cnt= 1주고 10을 빼준다
                cnt = 1; sum -= 10
            List.append(repr(sum))
        sum = 0  ##초기화
        for i in range(-len(B)-1,-len(A)-1,-1): ##남은 자리만큼
            sum = cnt + int(A[i])  ##A만 남았으니 A만 그대로 append
            cnt = 0
            if sum >= 10:
                cnt = 1; sum -= 10
            List.append(repr(sum))
        if cnt == 1:
            List.append(repr(1))
    else:  ##B가 더 길면
        for i in range(-1,-len(A)-1,-1):
            sum = int(A[i]) + int(B[i]) + cnt
            cnt = 0
            if sum >= 10:
                cnt = 1; sum -= 10
            List.append(repr(sum))
        sum = 0
        for i in range(-len(A)-1,-len(B)-1,-1):
            sum = cnt + int(B[i])
            cnt = 0
            if sum >= 10:
                cnt = 1; sum -= 10
            List.append(repr(sum))
        if cnt == 1:
            List.append(repr(1))

    for i in range(-1,-len(List)-1,-1):  ##append를 뒤에서 부터 해줘서 출력은 반대
        print(List[i],end="")

##덧셈의 원리를 알면 문자열을 정수형으로 바꿔서 풀 수 있었던 문제
##A와 B의 자리수에 따라 코드를 두번 써줘야돼서 번거로웠다.
##repr이란 함수를 배웠다. 숫자를 문자열로 바꿔준다.