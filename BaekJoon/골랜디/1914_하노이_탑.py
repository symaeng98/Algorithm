def hanoi(n, f, t):
    if n == 1:
        print(f, t)
        return
    hanoi(n-1, f, 6-f-t)
    print(f, t)
    hanoi(n-1, 6-f-t, t)

n = int(input())
print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3)
