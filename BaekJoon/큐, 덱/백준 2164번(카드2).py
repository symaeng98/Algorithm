##함수 선언 부분
import sys

def _push_X(q, data):
    q.append(data)
def _pop(q):
    global cnt
    tmp = q[cnt]
    cnt += 1
    return tmp
##변수 선언 부분
queue = []
cnt = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        _push_X(queue,i+1)

    while True:
        if len(queue)-cnt == 1:
            print(queue[cnt-1])
            break
        _pop(queue)
        _push_X(queue,_pop(queue))