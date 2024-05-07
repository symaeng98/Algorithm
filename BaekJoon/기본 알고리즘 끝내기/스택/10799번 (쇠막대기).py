arr = list(input())

block = []
result = 0
for i in range(len(arr)):
    if arr[i] == "(":
        block.append(('(', i))
    else:
        if arr[i-1] == "(":
            block.pop()
            result += len(block)
        else:
            block.pop()
            result += 1

print(result)