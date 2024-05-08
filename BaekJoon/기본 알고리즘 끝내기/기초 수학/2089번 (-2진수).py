n = int(input())
if n == 0 or n == 1:
    print(n)
else:
    result = []
    while n != 0:
        mod = n % (-2)
        if mod == 0:
            result.append("0")
            n //= -2
        else:
            result.append("1")
            n = n//(-2)+1
    result.reverse()

    print(''.join(result))