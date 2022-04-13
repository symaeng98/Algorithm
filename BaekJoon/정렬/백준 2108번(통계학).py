##함수 선언 부분
import sys


##변수 선언 부분
data = []
sum = 0
index = 0
count = []
max = -1
max_list = [] #max가 같은 값들 저장
cnt = 0
range1 = 0
##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    count = [0] * 10001 #각 수들의 빈도수 저장
    for i in range(N):
        a = int(sys.stdin.readline())
        if a < 0:
            count[4000 - a] += 1
        else:
            count[a] += 1
        sum += a #평균을 위한 합 계산
        data.append(a)
    data.sort() #오름차순 정렬해준다.
    if sum < 0:
        cnt = 1
        sum = -sum
    if (sum % N) / N >= 0.5: #반올림
        if cnt == 1:
            print(-((sum//N) + 1))
        else:
            print((sum // N) + 1)
    else:
        if cnt == 1:
            print(-(sum // N))
        else:
            print((sum // N))

    print(data[N // 2]) #중앙 값 출력


    for i in range(8001): #최빈값을 찾아준다.
        if max < count[i]:
            max = count[i]

    for i in range(8001): #찾은 최빈값으로 여러개 있을 경우를 구해준다.
        if max == count[i]:
            max_list.append(i)

    if len(max_list) == 1: #최빈값이 한개면
        if max_list[0] > 4000: #음수면
            print(4000 - max_list[0]) #음수로 출력
        else: #양수면 그대로 출력
            print(max_list[0])
    else: #최빈값이 여러개면
        max_len = len(max_list)

        if max_list[max_len - 2] > 4000: #오름차순으로 정렬되어 있기 때문에 맨 뒤에서 두번째 값이 음수면
            print(4000 - max_list[max_len - 2]) #자연스럽게 그 값이 최빈값들 중 두번째로 작은 값이 된다
        elif max_list[max_len - 1] > 4000: #맨 뒤에서 첫번째 값만 음수라면
            print(max_list[0]) #0번째 인덱스를 가진 값이 두번째로 작은 값
        else: #모두 양수라면
            print(max_list[1]) #1번째 인덱스를 가진 값이 두번째로 작은 값


    range1 = data[N - 1] - data[0]
    print(range1)


##코드를 너무 어렵게 짠 것 같아서 중간중간 틀린 출력 값이 나왔다. 짜잘한 실수만 아니었다면 더 빨리 풀었을 수 있었을 것 같다.
##두번째로 작은 값을 찾는 것이 음수가 포함되어 있어서 배열의 인덱스를 구할 때 어려웠다.
