##함수 선언 부분
import sys
def bs(A, num, start, end):
    if start > end: #종료 조건
        return 0
    mid = (start + end) // 2
    if A[mid] < num: #찾는 수가 더 크면
        return bs(A, num, mid+1, end) #mid에서 한칸 오른쪽을 start로 보낸다
    elif A[mid] > num: #작으면
        return bs(A, num, start, mid-1) #mid에서 한칸 왼쪽을 end로 보낸다
    else:
        cnt = 0
        for i in range(mid, end + 1):  # start에서 end까지
            if A[i] == num:  # 찾는 수의 개수를 세주고
                cnt += 1
            else:
                break
        for i in range(mid - 1, start - 1, -1):
            if A[i] == num:
                cnt += 1
            else:
                break
        return cnt  # return해준다

##변수 선언 부분
A = []
B = []
##메인 함수 부분
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    A = [int(x) for x in sys.stdin.readline().split()]
    M = int(sys.stdin.readline())
    B = [int(x) for x in sys.stdin.readline().split()]
    A.sort()
    n_dic = {}
    for n in A:
        start = 0
        end = len(A) - 1
        if n not in n_dic:
            n_dic[n] = bs(A, n, start, end)

    print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in B))


