import sys
input = sys.stdin.readline
from collections import deque

def push(q, k):
    q.append(k)

def pop(q):
    if len(q) == 0:
        print(-1)
    else:
        x = q.popleft()
        print(x)

def front(q):
    if len(q) == 0:
        print(-1)
    else:
        print(q[0])

def back(q):
    if len(q) == 0:
        print(-1)
    else:
        print(q[-1])

def size(q):
    print(len(q))

def empty(q):
    if len(q) == 0:
        print(1)
    else:
        print(0)

q = deque()
n = int(input())
for _ in range(n):
    order_arr = list(input().split())
    order = order_arr[0]

    if len(order_arr) == 2:
        k = int(order_arr[1])
    if order == "push":
        push(q, k)
    elif order == "pop":
        pop(q)
    elif order == "front":
        front(q)
    elif order == "back":
        back(q)
    elif order == "size":
        size(q)
    elif order == "empty":
        empty(q)
    else:
        print("error")