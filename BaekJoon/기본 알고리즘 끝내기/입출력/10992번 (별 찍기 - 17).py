n = int(input())
for i in range(1, n+1):
    for j in range(n-i-1, -1, -1):
        print(" ", end="")

    for j in range(i*2-1):
        if j == 0 or j == i*2-2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()