#N,K 입력
N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

#A는 오름차순, B는 내림차순으로 정렬한다.
A.sort()
B.sort(key=lambda x : -x)

#A의 원소가 더 작으면 swap
for i in range(K):
    if A[i]<B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

#A의 합을 출력
print(sum(A))