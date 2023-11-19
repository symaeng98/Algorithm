##함수 선언 부분##


##변수 선언 부분##
data = []
sum = 1
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    data = [[int(x) for x in input().split()]for y in range(N)]
    data.sort(key=lambda x: (x[1],x[0])) #끝나는 시간으로 오름차순 정렬하고 같으면 시작하는 시간으로 정렬
    end = data[0][1] #첫 번째값의 끝나는 시간을 저장

    for i in range(1,N):
        if data[i][0] >= end: #앞의 회의가 끝나는 시간보다 뒤에 시작하면
            sum += 1 #sum증가
            end = data[i][1] #회의 끝나는 시간 갱신
    print(sum)
