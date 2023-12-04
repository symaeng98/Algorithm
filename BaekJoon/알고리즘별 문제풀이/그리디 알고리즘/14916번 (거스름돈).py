n = int(input())

result = 1e9

for i in range((n//5)+1):
    nx = n - 5*i
    if nx % 2 == 0:
        result = min(result, i+nx//2)

if result == 1e9:
    print(-1)
else:
    print(result)