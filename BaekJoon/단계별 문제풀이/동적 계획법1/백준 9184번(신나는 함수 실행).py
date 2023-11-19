##함수 선언 부분##
def W(a, b, c):
    index = (a - 1) * 400 + (b - 1) * 20 + (c - 1) #구한 값을 캐싱하기 위한 index
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c >20:
        return W(20, 20, 20)
    elif (a < b) and (b < c):
        if w[index] == 0: #값이 캐싱되어있지 않으면
            w[index] = W(a,b,c-1) + W(a,b-1,c-1) - W(a,b-1,c) #값을 저장

        return w[index]
    else:
        if w[index] == 0:
            w[index] = W(a-1,b,c) + W(a-1,b-1,c) + W(a-1,b,c-1) - W(a-1,b-1,c-1)

        return w[index]
##변수 선언 부분##
w = [0]*10000

##메인 함수 부분##
if __name__ == "__main__":
    while True:
        a, b, c = map(int,input().split())
        if a == b == c == -1:
            break
        else:
            ans = W(a,b,c)
            print("w(%d, %d, %d) = %d"%(a,b,c,ans))
