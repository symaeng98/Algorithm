##함수 선언 부분##
def count(i,t):
    j = i
    cnt = 0
    while True:
        if j > t:
            break
        cnt += (t // j)
        j *= i
    return cnt

##변수 선언 부분##
N_cnt_2 = 0
N_cnt_5 = 0
M_cnt_2 = 0
M_cnt_5 = 0
M_N_cnt_2 = 0
M_N_cnt_5 = 0
##메인 함수 부분##
if __name__ == "__main__":
    N, M = map(int,input().split())
    N_cnt_2 = count(2,N)
    N_cnt_5 = count(5,N)
    M_cnt_2 = count(2,M)
    M_cnt_5 = count(5,M)
    M_N_cnt_2 = count(2,N-M)
    M_N_cnt_5 = count(5,N-M)
    print(min(N_cnt_5 - M_cnt_5 - M_N_cnt_5, N_cnt_2 - M_cnt_2 - M_N_cnt_2))