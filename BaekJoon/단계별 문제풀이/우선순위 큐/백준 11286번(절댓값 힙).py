##함수 선언 부분
import sys
import math
##변수 선언 부분
min_heap = []
cnt = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    min_heap = [-1] *100010
    for i in range(N):
        command = int(sys.stdin.readline())
        if command == 0:
            if cnt == 0: #들어있는 것이 없으면,
                print(0) #0출력
            else:
                print(min_heap[1])
                min_heap[1] = min_heap[cnt]
                min_heap[cnt] = -1 #pop후 저장
                cnt -= 1
                index = 1
                while index*2 <= cnt:
                    if (index*2+1) > cnt: #left child만 있는 경우에는
                        if abs(min_heap[index]) > abs(min_heap[index*2]): #left child값보다 크면,
                            tmp = min_heap[index] #교환
                            min_heap[index] = min_heap[index * 2]
                            min_heap[index * 2] = tmp
                            index *= 2
                        elif abs(min_heap[index]) == abs(min_heap[index*2]):
                            if min_heap[index] > min_heap[index*2]:
                                tmp = min_heap[index]  # 교환
                                min_heap[index] = min_heap[index * 2]
                                min_heap[index * 2] = tmp
                                index *= 2
                            else:
                                break
                        else:
                            break
                    elif abs(min_heap[index]) > min(abs(min_heap[index*2]),abs(min_heap[index*2+1])): #자식 노드의 최솟값보다 작으면,
                        if abs(min_heap[index*2]) < abs(min_heap[index*2+1]): #left child가 더 작으면,
                            tmp = min_heap[index] #교체
                            min_heap[index] = min_heap[index*2]
                            min_heap[index*2] = tmp
                            index *= 2
                        elif abs(min_heap[index*2]) == abs(min_heap[index*2+1]):
                            if min_heap[index*2] < min_heap[index*2+1]:
                                tmp = min_heap[index]  # 교체
                                min_heap[index] = min_heap[index * 2]
                                min_heap[index * 2] = tmp
                                index *= 2
                            else:
                                tmp = min_heap[index]
                                min_heap[index] = min_heap[index * 2 + 1]
                                min_heap[index * 2 + 1] = tmp
                                index = index * 2 + 1
                        else:
                            tmp = min_heap[index]
                            min_heap[index] = min_heap[index*2+1]
                            min_heap[index*2+1] = tmp
                            index = index * 2 + 1
                    elif abs(min_heap[index]) == min(abs(min_heap[index*2]),abs(min_heap[index*2+1])):
                        if abs(min_heap[index*2]) < abs(min_heap[index*2+1]):
                            if min_heap[index] > min_heap[index*2]:
                                tmp = min_heap[index]  # 교체
                                min_heap[index] = min_heap[index * 2]
                                min_heap[index * 2] = tmp
                                index *= 2
                            else:
                                break
                        else:
                            if min_heap[index] > min_heap[index*2+1]:
                                tmp = min_heap[index]  # 교체
                                min_heap[index] = min_heap[index*2+1]
                                min_heap[index*2+1] = tmp
                                index = index * 2 + 1
                            else:
                                break
                    else:
                        break

        else:
            cnt += 1 #원소 개수 증가
            min_heap[cnt] = command
            index = cnt
            while index > 1: #index부터 1보다 작아질 떄 까지 2로 나누어서 부모 노드로 이동
                if abs(min_heap[index]) < abs(min_heap[index//2]): #부모모다 작으면
                    tmp = min_heap[index] #교체
                    min_heap[index] = min_heap[index//2]
                    min_heap[index//2] = tmp
                    index //= 2
                elif abs(min_heap[index]) == abs(min_heap[index//2]):
                    if min_heap[index] < min_heap[index//2]:
                        tmp = min_heap[index]  # 교체
                        min_heap[index] = min_heap[index // 2]
                        min_heap[index // 2] = tmp
                        index //= 2
                    else:
                        break
                else:
                    break