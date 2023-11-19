##함수 선언 부분


##변수 선언 부분


##메인 함수 부분
if __name__ == "__main__":
    a1, a2 = map(int,input().split())
    b1, b2 = map(int,input().split())
    c1, c2 = map(int,input().split())
    if (a1 == b1 and a2 == c2) or (a1 == c1 and a2 == b2): #d의 위치의 대각선상에 있는 점이 a면
        d1 = b1 + c1 - a1
        d2 = b2 + c2 - a2
    elif (b1 == a1 and b2 == c2) or (b1 == c1 and b2 == a2):
        d1 = a1 + c1 - b1
        d2 = a2 + c2 - b2
    else:
        d1 = a1 + b1 - c1
        d2 = a2 + b2 - c2

    print("%d %d"%(d1,d2))


##예제 입력에 속아 원래 생각했던 풀이를 버리고 다른 방식으로 풀었다.
##길이를 이용해서 푸느라 생각보다 애를 먹었던 것 같다.