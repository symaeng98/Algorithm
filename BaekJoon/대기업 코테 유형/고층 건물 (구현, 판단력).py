INF = 1e9
n = int(input())
arr = list(map(int, input().split()))
answer = [0]*n

for i in range(n-1):
    max_lean = -INF
    for j in range(i+1, n):
        lean = (arr[j]-arr[i])/(j-i)
        if lean > max_lean:
            max_lean = max(max_lean, lean)
            answer[i] += 1
            answer[j] += 1

print(max(answer))