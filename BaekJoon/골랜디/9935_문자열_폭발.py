word = input()
bomb = input()
n = len(bomb)
stack = []

for s in word:
    stack.append(s)
    if stack[len(stack)-n:] == list(bomb):
        for _ in range(n):
            stack.pop()

if not stack:
    print("FRULA")
else:
    print(''.join(stack))

