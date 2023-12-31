t = int(input())
for _ in range(t):
    n = int(input())
    coins = [0]*4
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    while n != 0:
        if n >= quarter:
            coins[0] = n//quarter
            n -= quarter*coins[0]
        elif n >= dime:
            coins[1] = n//dime
            n -= dime*coins[1]
        elif n >= nickel:
            coins[2] = n//nickel
            n -= nickel*coins[2]
        else:
            coins[3] = n
            n -= coins[3]

    for c in coins:
        print(c, end=" ")
    print()