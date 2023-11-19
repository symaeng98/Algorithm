##함수 선언 부분##


##변수 선언 부분##
A = []
max_cnt = []
A_max = []
max_num = 0
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    A = [int(x) for x in input().split()]
    A.insert(0,0) #index의 편리성을 위해서 0을 넣어준다.
    max_cnt = [0] #초기값 설정
    A_max = [0]
    for i in range(1,N+1):
        max_num = 0
        for j in range(len(A_max)):
            if A[i] > A_max[j]: #자신보다 작은 수를 세준다.
                max_num += 1
            if max_num == max_cnt[j]: #만약 자신보다 작은 수의 개수가 같고
                if A[i] < A_max[j]: #이미 저장되어있는 값보다 작다면
                    A_max[j] = A[i] #저장되어있는 값을 갱신해준다.
                    max_num = 0 #초기화
                    break
                else:
                    max_num = -1 #자신보다 크거나 같으면 더 순회할 이유가 없기 때문에 탈출
                    break
        if max_num > 0: #자신이 제일 큰 수일 경우에
            A_max.append(A[i]) #값을 append해준다.
            max_cnt.append(max_num)
    print(max_cnt.pop())