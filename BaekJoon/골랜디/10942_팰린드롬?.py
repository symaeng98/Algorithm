import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

palindrome_map = [[0]*n for _ in range(n)]
for cnt in range(n):
    for i in range(n-cnt):
        j = i+cnt
        if i == j:
            palindrome_map[i][j] = 1
            continue
        if arr[i] == arr[j]:
            if i+1 == j:
                palindrome_map[i][j] = 1
            if palindrome_map[i+1][j-1]:
                palindrome_map[i][j] = 1

# for i in range(n7
# 1 2 1 3 1 2 1
# 4
# 1 3
# 2 5
# 3 3
# 5 7):
#     print(palindrome_map[i])

for _ in range(m):
    s, e = map(int, input().split())
    print(palindrome_map[s-1][e-1])

# 7
# 1 2 1 3 1 2 1
# 4
# 1 3
# 2 5
# 3 3
# 5 7