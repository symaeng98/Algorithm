n = int(input())
arr = list(map(int, input().split()))
result = [0]*n
stack = []

for i in range(n-1, -1, -1):
    while stack and (arr[stack[-1]] < arr[i]):
        result[stack[-1]] = i+1
        stack.pop()

    stack.append(i)

print(*result)
# 5
# 6 9 5 7 4