n = int(input())
calSum = 0
for _ in range(n):
    aStr, o, bStr = input().split()
    a, b = int(aStr), int(bStr)
    if o == '+':
        calSum += a+b
    elif o == '-':
        calSum += a-b
    elif o == '/':
        calSum += a//b
    elif o == '*':
        calSum += a*b
    else:
        print("error")
print(calSum)
