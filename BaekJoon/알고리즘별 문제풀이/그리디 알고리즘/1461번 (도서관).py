n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
left = []
right = []
max_dist = 0
for a in arr:
    max_dist = max(max_dist, abs(a))
for a in arr:
    if a < 0:
        left.append(-a)
    else:
        right.append(a)

right.sort(reverse=True)

res = 0
ind = 0
while ind < len(right):
    res += right[ind] * 2
    ind += m

ind = 0
while ind < len(left):
    res += left[ind] * 2
    ind += m

print(res - max_dist)