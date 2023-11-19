##함수 선언 부분
def Hanoi(num, _from, _to):
    if num == 1:
        print(_from, _to)
    else:
        Hanoi(num - 1, _from, 6 - _from - _to) #num - 1개를 1에서 2로 이동
        print(_from, _to) #제일 큰 판을 3으로 이동
        Hanoi(num - 1, 6 - _from - _to, _to) #2에서 3으로 이동
##변수 선언 부분
N = 0

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    print(2**N - 1)
    Hanoi(N, 1, 3)

##자료구조시간에 풀었던 기억은 났지만 다시 풀어보니 새로웠다. 너무 어렵게 생각했다. 재귀의 특징을
##이용하지 않고 케이스를 너무 구체적으로 들어가서 오래 걸렸던 것 같다. 차라리 구글링을 하고 이해를 할 걸 그랬다.