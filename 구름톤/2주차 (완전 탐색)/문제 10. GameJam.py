n = int(input())
gx, gy = map(int, input().split())
px, py = map(int, input().split())
gx, gy = gx-1, gy-1
px, py = px-1, py-1

board = [list(input().split()) for _ in range(n)]
g_visit_list = []
p_visit_list = []

def get_visit_list(x, y, visit_list):
    while (x,y) not in visit_list:
        visit_list.append((x,y))
        cmd = board[x][y]
        cmd_move = int(cmd[:-1])
        cmd_direction = cmd[-1]
        for i in range(cmd_move-1):
            if cmd_direction == 'L':
                y = y-1
                if y < 0:
                    y = n-1
            elif cmd_direction == 'R':
                y = y+1
                if y >= n:
                    y = 0
            elif cmd_direction == 'U':
                x = x-1
                if x < 0:
                    x = n-1
            elif cmd_direction == 'D':
                x = x+1
                if x >= n:
                    x = 0
            else:
                print("error")
            if (x,y) in visit_list:
                return
            visit_list.append((x, y))

        if cmd_direction == 'L':
            y = y-1
            if y < 0:
                y = n-1
        elif cmd_direction == 'R':
            y = y+1
            if y >= n:
                y = 0
        elif cmd_direction == 'U':
            x = x-1
            if x < 0:
                x = n-1
        elif cmd_direction == 'D':
            x = x+1
            if x >= n:
                x = 0
        else:
            print("error")

get_visit_list(gx, gy, g_visit_list)
get_visit_list(px, py, p_visit_list)
g_score = len(g_visit_list)
p_score = len(p_visit_list)

if g_score > p_score:
    print("goorm " + str(g_score))
else:
    print("player " + str(p_score))