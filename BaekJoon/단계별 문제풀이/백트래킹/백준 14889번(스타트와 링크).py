##함수 선언 부분##
def Team(index):
    global sumA, sumB, min
    if index == N//2:
        B = [] #지역변수 B배열 선언
        for i in range(N): #구한 A팀을 이용해서 B팀을 구해준다.
            if i in A:
                continue
            else:
                B.append(i)
        A_chemistry(A) #A팀의 능력치를 구한다.
        B_chemistry(B) #B팀의 능력치를 구한다.
        if sumA > sumB: #gap이 음수가 나오지 않게 조건을 만들어준다.
            gap = sumA - sumB
        else:
            gap = sumB - sumA
        if min > gap: #능력치의 최솟값을 갱신해준다.
            min = gap
        sumA = 0 #초기화
        sumB = 0
        del(B) #B 삭제
    else:
        for i in range(N):
            if i in A: #중복되면 무시
                continue
            if index >= 1: #만약 A[0]이 존재하면
                if A[0] > 0: #A[0]이 0인 경우만 탐색을 할 것이기 때문에 0보다 크면 무시
                    continue
                if i < A[index-1]: #오름차순인 경우에만 탐색을 하기위한 조건
                    continue
            A.append(i)
            Team(index+1)
            A.pop()


def A_chemistry(A):
    global sumA
    if len(A_chemi) == 2: #선수 두명의 값이 모두 들어오면
        sumA += data[A_chemi[0]][A_chemi[1]] #각 선수끼리의 케미를 더해주고
        return sumA #반환
    else:
        for i in A:
            if i in A_chemi: #중복되면 무시
                continue
            A_chemi.append(i)
            A_chemistry(A)
            A_chemi.pop()


def B_chemistry(B): #A와 동일
    global sumB
    if len(B_chemi) == 2:
        sumB += data[B_chemi[0]][B_chemi[1]]
        return sumB
    else:
        for i in B:
            if i in B_chemi:
                continue
            B_chemi.append(i)
            B_chemistry(B)
            B_chemi.pop()
##변수 선언 부분##
data = []
N = 0
A = []
A_chemi = []
B_chemi = []
sumA = 0
sumB = 0
min = 1000000
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    data = [[int(x) for x in input().split()]for _ in range(N)]
    members = [int(x) for x in range(N)]
    Team(0)
    print(min)