n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, 1+(m-1)//2))
elif m <= 6:
    print(min(4, m))
else:
    print(5 + (m-7))