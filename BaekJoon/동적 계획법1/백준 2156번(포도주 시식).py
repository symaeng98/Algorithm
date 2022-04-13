##함수 선언 부분##
import sys
##변수 선언 부분##
grape = []
grape_max = []
case1 = 0
case2 = 0
case3 = 0
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        grape.append(int(input()))

    grape_max.append(grape[0])
    if N == 1:
        print(grape_max.pop())
        sys.exit(0)
    grape_max.append(grape[1] + grape[0])
    if N == 2:
        print(grape_max.pop())
        sys.exit(0)
    grape_max.append(max((grape[0]+grape[1]),(grape[0]+grape[2]),(grape[1]+grape[2])))
    if N == 3:
        print(grape_max.pop())
        sys.exit(0)
    grape_max.append(max((grape[0]+grape[1]+grape[3]),(grape[0]+grape[2]+grape[3]),(grape[1]+grape[2])))
    if N == 4:
        print(grape_max.pop())
        sys.exit(0)
    for i in range(4,N):
        case1 = grape_max[i-3] + grape[i-1] + grape[i]
        case2 = grape_max[i-2] + grape[i]
        case3 = grape_max[i-4] + grape[i-2] + grape[i-1]
        grape_max.append(max(case1,case2,case3))
    print(grape_max.pop())
