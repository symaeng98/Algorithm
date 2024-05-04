n = int(input())
for i in range(1, n+1):
    for j in range(n-i-1, -1, -1):
        print(" ", end="")
    for j in range(i*2-1):
        if j % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()