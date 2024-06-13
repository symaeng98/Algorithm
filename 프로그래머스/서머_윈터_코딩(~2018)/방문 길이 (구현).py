def solution(dirs):
    move_dict = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
    x, y = 0, 0
    visited = []
    cnt = 0
    for direction in dirs:
        dx, dy = move_dict[direction]
        nx, ny = x+dx, y+dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x,y,nx,ny) not in visited and (nx,ny,x,y) not in visited:
                cnt += 1
                visited.append((x,y,nx,ny))
            x, y = nx, ny

    return cnt