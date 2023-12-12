n, k = map(int, input().split())
arr = list(map(int, input().split()))

now = []

result = 0
for i in range(k):
    if arr[i] in now:
        continue

    if len(now) < n:
        now.append(arr[i])
        continue

    max_index = 0
    index = 0
    for j in range(n):
        if now[j] not in arr[i:]:
            index = j
            break

        if arr[i:].index(now[j]) > max_index:
            max_index = arr[i:].index(now[j])
            index = j

    now[index] = arr[i]
    result += 1

print(result)