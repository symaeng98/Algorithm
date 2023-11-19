##함수 선언 부분
def star(num, a, b):
   if num == 1:
       is_star[a][b] = 1 #좌표에 1을 넣어준다
   else:
       for a1 in range(3):
           for b1 in range(3):
               if a1 != 1 or b1 != 1: #가운데는 비워야한다
                   star(num//3, a + a1 * num//3, b + b1 * num//3)
                   #들어온 좌표 + 0부터 2에 num//3을 곱한 값을 더해주어 좌표를 구한다


##변수 선언 부분
N = 0
max_num = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    is_star = [[0 for col in range(N) ] for row in range(N)]
    max_num = N
    star(N, 0, 0)
    for i in range(0, N):
        for j in range(0, N):
            if is_star[i][j]:
                print("*",end="")
            else:
                print(" ",end="")
        print("")


##그냥 for문으로도 풀어보아도 까다롭고 헷갈리는 문제였다. 재귀함수를 사용할 수 있겠다고 생각이 바로 들었지만
##막상 for문과 재귀를 함께 써 보니 어려웠던 것 같다. 또한 브루트 포스 느낌으로 메모리 생각없이 반복문을
##돌려서 풀었지만 역시 시간초과가 떴다. 구글의 도움을 조금 받아서 힌트를 얻어서 풀어보니 너무 어렵게만
##생각한 것 아닌가 싶었다.