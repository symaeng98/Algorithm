##함수 선언 부분


##변수 선언 부분
is_const = 0 #생성자가 있는 지 확인 없으면 0출력
N = 0
digits = 0 #자릿수
sum = 0 #분해합
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    for i in range(1, N):
        divide = i #i와 N을 보존해야되므로 나눠도 되는 변수 설정
        M = i
        digits = 0
        sum = 0
        while M != 0: #자릿수를 구해준다.
            M = M // 10
            digits += 1
        for j in range(1, digits + 1): #digits만큼 반복
            sum += divide % 10
            divide //= 10
        sum += i #자기 자신을 더해준다
        if sum == N:
            is_const = 1 #생성자가 존재한다
            print(i)
            break
    if not is_const: #생성자가 없으면
        print(0)