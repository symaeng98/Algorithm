a, b = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))
arr.reverse()

now = 1
ten = 0
for ar in arr:
    ten += ar*now
    now *= a

result = []
while ten > 0:
    mod = ten % b
    result.append(str(mod))
    ten //= b

result.reverse()
print(' '.join(result))