n = int(input())
answer = 0
stack = []
skylines = []
for i in range(n):
    skylines.append(int(input().split()[1]))

for sl in skylines:
    while stack and stack[-1] > sl:
        answer += 1
        stack.pop()
    if stack and stack[-1] == sl:
        continue
    stack.append(sl)

while stack:
    if stack[-1] > 0:
        answer += 1
    stack.pop()

print(answer)