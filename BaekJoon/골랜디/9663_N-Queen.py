from collections import defaultdict

n = int(input())

result = 0

is_used_col = [False]*n
add_cross_map = defaultdict(bool)
sub_cross_map = defaultdict(bool)

def nqueen(now, cnt):
    global result

    if cnt == n:
        result += 1
        return

    for i in range(n):
        if is_used_col[i] or add_cross_map[now+i] or sub_cross_map[now-i]:
            continue
        is_used_col[i] = True
        add_cross_map[now+i] = True
        sub_cross_map[now-i] = True
        nqueen(now+1, cnt+1)
        is_used_col[i] = False
        add_cross_map[now+i] = False
        sub_cross_map[now-i] = False


nqueen(0, 0)

print(result)