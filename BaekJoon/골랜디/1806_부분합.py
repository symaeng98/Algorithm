n, s = map(int, input().split())
arr = list(map(int, input().split()))
add_arr = [0]*(n+1)
add_arr[1] = arr[0]
for i in range(1, n+1):
    add_arr[i] = arr[i-1] + add_arr[i-1]

left = 0
right = 0
min_length = 1e9

for right in range(1, n+1):
    if add_arr[right] - add_arr[left] < s:
        continue

    while add_arr[right] - add_arr[left] >= s:
        left += 1

    min_length = min(min_length, right-left+1)

if min_length == 1e9:
    print(0)
else:
    print(min_length)

# 10 15
# 5 1 3 5 10 7 4 9 2 8