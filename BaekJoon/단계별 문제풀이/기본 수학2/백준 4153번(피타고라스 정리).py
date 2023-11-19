##함수 선언 부분


##변수 선언 부분
triangle = []

##메인 함수 부분
if __name__ == "__main__":
    while True:
        triangle = [x for x in map(int,input().split())]
        if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
            break
        else:
            triangle.sort()
            if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
                print("right")
            else:
                print("wrong")

#피타고라스 정리를 알면 쉽게 풀 수 있다.
