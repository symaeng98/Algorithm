n, l = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()

for fruit in fruits:
    if l < fruit:
        break
    l += 1
print(l)