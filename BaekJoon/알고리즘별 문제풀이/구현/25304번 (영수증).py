total_price = int(input())
n = int(input())
for _ in range(n):
    p, c = map(int, input().split())
    total_price -= p*c
if total_price == 0:
    print("Yes")
else:
    print("No")