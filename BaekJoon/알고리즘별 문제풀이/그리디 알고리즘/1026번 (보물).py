n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b_sorted = sorted(b, reverse=True)

result =0
for i in range(len(a)):
    result += a[i]*b_sorted[i]

print(result)