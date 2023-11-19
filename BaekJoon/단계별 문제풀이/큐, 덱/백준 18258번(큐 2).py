##함수 선언 부분
import sys

def _push_X(q, data):
    q.append(int(data))
def _pop(q):
    global cnt
    if len(q) == cnt:
        print(-1)
    else:
        print(q[cnt])
        cnt += 1
def _size(q):
    print(len(q)-cnt)
def _empty(q):
    if len(q)-cnt == 0:
        print(1)
    else:
        print(0)
def _back(q):
    if len(q)-cnt == 0:
        print(-1)
    else:
        print(q[len(q)-1])
def _front(q):
    if len(q)-cnt == 0:
        print(-1)
    else:
        print(q[cnt])
##변수 선언 부분
command = []
queue = []
cnt = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        command = sys.stdin.readline().split()
        if command[0] == "push":
            _push_X(queue, command[1])
        elif command[0] == "pop":
            _pop(queue)
        elif command[0] == "size":
            _size(queue)
        elif command[0] == "empty":
            _empty(queue)
        elif command[0] == "front":
            _front(queue)
        else:
            _back(queue)