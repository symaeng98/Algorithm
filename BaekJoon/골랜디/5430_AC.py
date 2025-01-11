from collections import deque

t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    tmp = input()
    tmp = tmp.lstrip("[")
    tmp = tmp.rstrip("]")
    arr = deque(tmp.split(",")) if n != 0 else deque()
    popleft = True
    is_error = False
    for c in p:
        if c == 'R':
            popleft = False if popleft else True
        elif c == 'D':
            if len(arr) == 0:
                is_error = True
                break
            if popleft:
                arr.popleft()
            else:
                arr.pop()

    if is_error:
        print("error")
    else:
        if not popleft:
            arr.reverse()
        print("[", end="")
        print(','.join(arr), end="")
        print("]", end="")
        print()