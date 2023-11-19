##함수 선언 부분


##변수 선언 부분
N = 0
M = 0
gap_min = 300000
sum = 0
gap = 0
sum_min = 0
##메인 함수 부분
if __name__ == "__main__":
    N, M = map(int, input().split())
    card = [x for x in map(int,input().split())]
    for i in range(0, N - 2): #처음부터 마지막 2개 전까지
        for j in range(i+1, N - 1): #마지막 1개 전까지
            for k in range(j+1, N): #마지막까지
                sum = card[i] + card[j] + card[k] #합을 구해준다
                gap = M - sum
                if gap >= 0:
                    if gap_min > gap: #차이가 더 작으면
                        gap_min = gap #값들 저장
                        sum_min = sum

    print(sum_min)

##문제를 잘못 읽어서 계속 틀렸다. 문제를 꼼꼼히 읽자!