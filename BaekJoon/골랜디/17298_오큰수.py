n = int(input())
arr = list(map(int, input().split()))

result = [-1]*n
stack = []
for i in range(n):
    # 스택이 비어있지 않고, 현재 원소가 스택에 들어있는 원소보다 큰 경우에 계속해서 갱신
    while stack and (arr[i] > arr[stack[-1]]):
        index = stack.pop()
        result[index] = arr[i]

    stack.append(i)

print(*result)


# 4
# 9 5 4 8