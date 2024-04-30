n = int(input())
arr = list(map(int, input().split()))

result = 0
start, end = 0, 0
visited = [False] * 100001
while start < n and end < n:
    if not visited[arr[end]]:
        visited[arr[end]] = True
        result += end - start + 1
        end += 1
    else:
        visited[arr[start]] = False
        start += 1

print(result)