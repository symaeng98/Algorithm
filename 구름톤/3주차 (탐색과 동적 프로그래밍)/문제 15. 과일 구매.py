n, k = map(int, input().split())
fruit_list = []

for _ in range(n):
    p, c = map(int, input().split())
    fruit_list.append((p, c))

sorted_fruit_list = sorted(fruit_list, key=lambda x:(x[1]//x[0], x[0]), reverse = True)

result = 0
cost = 0
for f in sorted_fruit_list:
    p, c = f[0], f[1]
    if cost + p > k:
        dif = k - cost
        result += dif * (c // p)
        break
    result += c
    cost += p
print(result)