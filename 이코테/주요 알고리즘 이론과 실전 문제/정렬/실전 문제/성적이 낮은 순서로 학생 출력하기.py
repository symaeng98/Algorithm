#N 입력
N = int(input())

#이름, 점수 입력
arr = []

for i in range(N):
    data = input().split()
    arr.append(tuple(data))


#lambda를 이용하여 정렬
arr.sort(key=lambda x:x[1])

#출력
for a in arr:
    print(a[0],end=" ")