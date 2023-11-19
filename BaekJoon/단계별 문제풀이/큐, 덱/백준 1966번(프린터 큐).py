##함수 선언 부분
def enqueue(q, item):
    q.append(item)
def dequeue(q):
    global cnt
    tmp = q[cnt]
    cnt += 1
    return tmp
##변수 선언 부분
imp = []
cnt = 0
indexes = []
cnt_num = 0
isRight = 1
##메인 함수 부분
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, p = map(int, input().split())
        indexes = []
        cnt = 0
        cnt_num = 0
        isRight = 1
        for j in range(N):
            indexes.append(j) #중요도의 인덱스 입력
        imp = [int(x) for x in input().split()] #중요도 입력
        while True:
            for j in range(cnt, len(imp)):
                if imp[cnt] < imp[j]:
                    enqueue(imp, dequeue(imp))
                    cnt -= 1
                    enqueue(indexes, dequeue(indexes))
                    isRight = 0
                    break
            if isRight:
                cnt_num += 1
                a = dequeue(indexes)
                cnt -= 1
                dequeue(imp)
                if a == p:
                    print(cnt_num)
                    break
            isRight = 1
        del(indexes)