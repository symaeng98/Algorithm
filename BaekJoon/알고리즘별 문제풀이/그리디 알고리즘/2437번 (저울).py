n = int(input())
arr = list(map(int, input().split()))
arr.sort()

valid = [0]*n
answer = 0
if arr[0] != 1:
    answer = 1
else:
    valid[0] = 1
    for i in range(1, n):
        if valid[i-1]+1 < arr[i]:
            answer = valid[i-1]+1
            break
        valid[i] = valid[i-1]+arr[i]

if answer != 0:
    print(answer)
else:
    print(valid[n-1]+1)