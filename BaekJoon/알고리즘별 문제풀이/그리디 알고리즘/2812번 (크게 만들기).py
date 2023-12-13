n, k = map(int, input().split())
arr = list(map(int, input()))

stack = []
for a in arr:
    while k > 0 and stack and stack[-1] < a:
        stack.pop()
        k -= 1
    stack.append(a)

if k > 0:
    for i in range(len(stack)-k):
        print(stack[i], end="")
else:
    for s in stack:
        print(s, end="")