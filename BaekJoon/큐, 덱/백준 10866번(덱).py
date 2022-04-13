##함수 선언 부분
import sys
def push_front_X(dq, item):
    dq.insert(0,item)
def push_back_X(dq, item):
    dq.append(item)
def pop_front(dq):
    if len(dq) == 0:
        print(-1)
    else:
        print(dq.pop(0))
def pop_back(dq):
    if len(dq) == 0:
        print(-1)
    else:
        print(dq.pop(-1))
def size(dq):
    print(len(dq))
def empty(dq):
    if len(dq) == 0:
        print(1)
    else:
        print(0)
def front(dq):
    if len(dq) == 0:
        print(-1)
    else:
        print(dq[0])
def back(dq):
    if len(dq) == 0:
        print(-1)
    else:
        print(dq[-1])
##변수 선언 부분
command = []
dequeue = []
##메인 함수 부분
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        command = sys.stdin.readline().split()
        if command[0] == "push_back":
            push_back_X(dequeue, command[1])
        elif command[0] == "push_front":
            push_front_X(dequeue, command[1])
        elif command[0] == "pop_front":
            pop_front(dequeue)
        elif command[0] == "pop_back":
            pop_back(dequeue)
        elif command[0] == "size":
            size(dequeue)
        elif command[0] == "empty":
            empty(dequeue)
        elif command[0] == "front":
            front(dequeue)
        else:
            back(dequeue)