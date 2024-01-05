from bisect import bisect_left, bisect_right

t = int(input())
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a_arr = []
for i in range(n):
    x = a[i]
    a_arr.append(x)
    for j in range(i+1, n):
        x += a[j]
        a_arr.append(x)

b_arr = []
for i in range(m):
    x = b[i]
    b_arr.append(x)
    for j in range(i+1, m):
        x += b[j]
        b_arr.append(x)

a_arr.sort()
b_arr.sort()

result = 0
for i in range(len(a_arr)):
    l = bisect_left(b_arr, t-a_arr[i])
    r = bisect_right(b_arr, t-a_arr[i])

    result += (r-l)

print(result)