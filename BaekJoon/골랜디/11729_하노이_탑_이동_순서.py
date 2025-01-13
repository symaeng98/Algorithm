n = int(input())

def hanoi(num, f, t):
    if num == 1:
        print(f, t)
        return

    hanoi(num-1, f, 6-f-t)
    print(f, t)
    hanoi(num-1, 6-f-t, t)

print(2**n-1)
hanoi(n, 1, 3)
