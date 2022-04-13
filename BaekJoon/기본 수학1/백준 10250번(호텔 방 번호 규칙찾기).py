##함수 선언 부분##

##변수 선언 부분##
T = 0
H = 0
W = 0
N = 0
hoe = 1
floor = 0
##메인 함수 부분##
if __name__ == "__main__" :
    T = int(input())
    for i in range (0, T):
        hoe = 1
        floor = 0
        H, W, N = map(int,input().split())
        while True :
            if H * hoe >= N: ##호에 높이를 곱한것 만큼이 배정할 방보다 커지면 break
                break
            hoe += 1
        floor = N - (hoe - 1) * H ##하나 증가해서 갔기때문에 hoe - 1

        if hoe < 10: ##한자리수는 0을 붙여야한다. ex)202호
            print(f"{floor}{0}{hoe}")
        else :
            print(f"{floor}{hoe}")

##어렵지 않았지만 예시가 별로 없어서 한번 틀리면 반례를 찾기가 힘들었던 문제.
##f-string을 처음 혼자서 써본 문제 꽤 편하다