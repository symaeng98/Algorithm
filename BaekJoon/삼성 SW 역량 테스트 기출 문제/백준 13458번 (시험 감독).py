import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

result = n
for i in range(n):
    arr[i] -= b
    if arr[i] > 0:
        if arr[i] % c != 0:
            result += arr[i]//c + 1
        else:
            result += arr[i]//c

print(result)