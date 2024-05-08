a, b = map(int, input().split())

mod = a % b
while mod > 0:
    a = b
    b = mod
    mod = a % b

print('1' * b)