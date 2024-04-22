import copy
from collections import deque

s = list(input())
n = len(s)
q = deque(s)
cnt_list = []
for i in range(n):
    left = 0
    right = n-1
    cnt = 0
    tmp = copy.deepcopy(q)
    while left < right:
        if tmp[left] != "a":
            left += 1
            continue
        if tmp[right] != "b":
            right -= 1
            continue

        tmp[left] = "b"
        tmp[right] = "a"
        cnt += 1

    cnt_list.append(cnt)
    q.append(q.popleft())

print(min(cnt_list))