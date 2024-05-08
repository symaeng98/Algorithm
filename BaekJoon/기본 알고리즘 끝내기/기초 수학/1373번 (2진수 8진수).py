arr = list(input())
arr.reverse()
result = []
index = 0
while index < len(arr):
    x = arr[index:index+3]
    tmp = 0
    for i in range(len(x)):
        tmp += int(x[i])*2**i

    result.append(str(tmp))
    index += 3
result.reverse()
print(''.join(result))