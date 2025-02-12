tmp = input()

result = []
stack = []
for s in tmp:
    if s == '(':
        stack.append(s)
    elif s in ['+', '-']:
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.append(s)
    elif s in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            result.append(stack.pop())
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    else:
        result.append(s)
    # print(stack)

while stack:
    result.append(stack.pop())

print(''.join(result))
