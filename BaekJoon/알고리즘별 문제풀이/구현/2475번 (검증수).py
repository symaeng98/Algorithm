arr = list(map(int, input().split()))
result = 0
for a in arr:
    result += a**2

print(result%10)