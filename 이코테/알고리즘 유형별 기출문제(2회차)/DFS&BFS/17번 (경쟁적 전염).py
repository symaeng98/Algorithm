n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus_loc = [[] for _ in range(k+1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus_loc[arr[i][j]].append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def move():
    for i in range(1, k+1):
        new_virus_loc = []
        while virus_loc[i]:
            x, y = virus_loc[i].pop()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 0:
                        new_virus_loc.append((nx, ny))
                        arr[nx][ny] = i
        virus_loc[i] = new_virus_loc

for _ in range(s):
    move()

print(arr[x-1][y-1])