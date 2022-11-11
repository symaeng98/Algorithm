n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 1, 1, 2, 3, 9

result = 1

for a in arr:
    if result < a:
        break
    result += a

print(result)