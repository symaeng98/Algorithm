##함수 선언 부분


##변수 선언 부분


##메인 함수 부분
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int,input().split())
        d = ((x2 - x1)**2 +(y2-y1)**2)
        ra = (r1 + r2)**2
        rb = (r1 - r2)**2

        if d == 0: #중심이 같을 때
            if (r1 == r2):
                print(-1) #한 원이 다른 원을 포함
            else:
                print(0)
        else: #중심이 다를 때
            if (d == ra) or (d == rb): #한 점만 겹칠 때
               print(1)
            elif((d < ra) and (d > rb)): #두 점이 겹칠 때
                print(2)
            else:
                print(0)


##쉬운 문젠데 왜 정답 비율이 낮나 했는데, 조건문을 잘 써야 풀 수 있는 문제였다. 기하에 대한 문제라기 보다는
##조건문의 중요성에 대해서 잘 알게 되었다.