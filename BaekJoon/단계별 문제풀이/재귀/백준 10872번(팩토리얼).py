##함수 선언 부분
def factorial(num, sum):
    if num == 1 or num == 0:
        return sum
    else:
        sum *= num
        return factorial(num-1, sum) #sum과 num-1을 인자로 보내줘서 계산

##변수 선언 부분
N = 0
ans = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    sum = 1
    ans = factorial(N, sum)
    print(ans)


##인자를 두개나 써서 그렇게 좋은 코드같지는 않다
##return해줄 때 return num * factorial(num-1)을 해주면 더 쉽게 짤 수 있다.