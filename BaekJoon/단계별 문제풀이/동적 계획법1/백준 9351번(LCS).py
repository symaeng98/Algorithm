##함수 선언 부분##


##변수 선언 부분##
st1 = []
st2 = []
dp = []
##메인 함수 부분##
if __name__ == "__main__":
    st1 = input()
    st2 = input()
    dp = [[0]*(len(st1)+1) for x in range(len(st2)+1)]

    for i in range(1,len(st2)+1): #각 st1의 알파벳에 따른 st2의 알파벳을 비교해야하기 때문에
        for j in range(1,len(st1)+1): #st2에 대한 반복문 안에 st1에 대한 반복문을 넣어준다.
            if st2[i-1] == st1[j-1]: #같은 알파벳이면,
                dp[i][j] = dp[i-1][j-1] + 1 #이전 값에 1을 더한 값을 넣어준다.
            else: #다른 알파벳이면,
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) #행에 대해 이전 값과 열에 대해 이전 값 중에서 큰 값을 넣어준다.

    print(dp[-1][-1])

    for i in range(len(st2)+1):
        for j in range(len(st1)+1):
            print(dp[i][j],end=" ")
        print("")