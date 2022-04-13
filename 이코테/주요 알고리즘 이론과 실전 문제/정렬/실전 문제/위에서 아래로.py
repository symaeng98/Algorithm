#N 입력받기
N = int(input())

#N개의 정수 저장
arr = []
for i in range(N):
    arr.append(int(input()))

#arr를 내림차순으로 정렬(lambda 이용)
arr.sort(key=lambda x:-x)

#출력
for i in arr:
    print(i,end=" ")
