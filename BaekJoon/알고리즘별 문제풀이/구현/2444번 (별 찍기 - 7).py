n = int(input())

for i in range(1, n):
    print(" "*(n-i), end="")
    print("*"*(i*2-1), end="")
    print()


for i in range(n, 0, -1):
    print(" "*(n-i), end="")
    print("*"*(i*2-1), end="")
    print()
