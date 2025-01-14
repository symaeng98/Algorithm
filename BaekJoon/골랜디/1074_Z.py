n, r, c = map(int, input().split())
result = 0


def z(n, x, y):
    global result
    if n == 0:
        return 0
    cre = 2**(n-1)
    nx, ny = x % cre, y % cre

    bx, by = x-cre, y-cre
    if bx < 0 and by < 0:
        k = 0
    elif bx < 0 and by >= 0:
        k = 1
    elif bx >= 0 and by < 0:
        k = 2
    else:
        k = 3

    return (cre**2)*k + z(n-1, nx, ny)


print(z(n, r, c))