##함수 선언 부분


##변수 선언 부분
A = []
stack = []
ans = []
top = -1
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = [-1] * N #ans배열은 모두 -1로 초기화
    for i in range(N):
        while (top != -1) and (A[i]>A[stack[top]]): #스택이 비어있지 않고, 스택의 top이 가리키는 인덱스의 A값이
            ans[stack.pop()] = A[i] #현재 탐색하는 인덱스의 A값보다 작으면, A[i]값을 스택의 top이 가리키는 인덱스의 값을 pop해서 나온 인덱스의 ans에 넣어준다.
            top -= 1
        stack.append(i) #탐색중인 값이 더 작으면 인덱스를 push해준다.
        top += 1

    print(*ans)