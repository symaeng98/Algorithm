import sys

prime = [True]*1000001
prime[1] = False
for i in range(2, int(1000001**0.5)+1):
    if prime[i]:
        for j in range(i*2, 1000001, i):
            prime[j] = False

while True:
    x = int(sys.stdin.readline())
    if x == 0:
        break

    flag = False
    for i in range(3, (x//2)+1, 2):
        if prime[i] and prime[x-i]:
            print(f"{x} = {i} + {x-i}")
            flag = True
            break
    if not flag:
        print("Goldbach's conjecture is wrong.")
