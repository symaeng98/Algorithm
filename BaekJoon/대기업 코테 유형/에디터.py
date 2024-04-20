stack_left = list(input())
m = int(input())
stack_right = []
for _ in range(m):
    tmp = list(input().split())
    if tmp[0] == "L":
        if len(stack_left) != 0:
            stack_right.append(stack_left.pop())
    elif tmp[0] == "D":
        if len(stack_right) != 0:
            stack_left.append(stack_right.pop())
    elif tmp[0] == "B":
        if len(stack_left) != 0:
            stack_left.pop()
    elif tmp[0] == "P":
        stack_left.append(tmp[1])
stack_right.reverse()

print(''.join(stack_left+stack_right))