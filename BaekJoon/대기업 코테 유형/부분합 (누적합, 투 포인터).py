n, s = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0]*n
sum_arr[0] = arr[0]
for i in range(1, n):
    arr[i] += arr[i-1]
arr.insert(0, 0)

left = 0
right = 0
result = []
while left < n+1 and right < n+1:
    if arr[right]-arr[left] < s:
        right += 1
    else:
        result.append(right-left)
        left += 1

if len(result) == 0:
    print(0)
else:
    print(min(result))