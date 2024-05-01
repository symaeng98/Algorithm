n = int(input())
arr = [input() for _ in range(n)]

s_arr = []
for i in range(n):
    s_arr.append((arr[i], i))
s_arr = sorted(s_arr)

length = [0]*n
max_value = -1
for i in range(n-1):
    cnt = 0
    for j in range(min(len(s_arr[i][0]), len(s_arr[i+1][0]))):
        if s_arr[i][0][j] != s_arr[i+1][0][j]:
            break
        cnt += 1
    max_value = max(max_value, cnt)

    length[s_arr[i][1]] = max(length[s_arr[i][1]], cnt)
    length[s_arr[i+1][1]] = max(length[s_arr[i+1][1]], cnt)

max_index = length.index(max_value)
max_head = arr[max_index][:max_value]
print(arr[max_index])
for i in range(n):
    if i != max_index and max_value == length[i] and arr[i][:max_value] == max_head:
        print(arr[i])
        break