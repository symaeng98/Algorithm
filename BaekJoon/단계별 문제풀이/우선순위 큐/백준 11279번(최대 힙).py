##함수 선언 부분
import sys
##변수 선언 부분
max_heap = []
cnt = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    max_heap = [-1] *100010
    for i in range(N):
        command = int(sys.stdin.readline())
        if command == 0:
            if cnt == 0: #들어있는 것이 없으면,
                print(0) #0출력
            else:
                print(max_heap[1])
                max_heap[1] = max_heap[cnt]
                max_heap[cnt] = -1 #pop후 저장
                cnt -= 1
                index = 1
                while index*2 <= cnt:
                    if max_heap[index] < max(max_heap[index*2],max_heap[index*2+1]): #자식 노드의 최대값보다 작으면,
                        if max_heap[index*2] > max_heap[index*2+1]:
                            tmp = max_heap[index]
                            max_heap[index] = max_heap[index*2]
                            max_heap[index*2] = tmp
                            index *= 2
                        else:
                            tmp = max_heap[index]
                            max_heap[index] = max_heap[index*2+1]
                            max_heap[index*2+1] = tmp
                            index = index * 2 + 1
                    else:
                        break

        else:
            cnt += 1
            max_heap[cnt] = command
            index = cnt
            while index > 1:
                if max_heap[index] > max_heap[index//2]:
                    tmp = max_heap[index]
                    max_heap[index] = max_heap[index//2]
                    max_heap[index//2] = tmp
                index //= 2