import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
answer = []

index_map = [0]*(n+1)  # 미리 인덱스 맵 만들어두기
for i in range(n):
    index_map[in_order[i]] = i


def pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    answer.append(post_order[post_end])
    k = index_map[post_order[post_end]]

    left = k - in_start  # 개수로 판단
    right = in_end - k

    pre_order(in_start, in_start+left-1, post_start, post_start+left-1)
    pre_order(in_end-right+1, in_end, post_end-right, post_end-1)


pre_order(0, n-1, 0, n-1)

print(*answer)
# 3
# 1 2 3
# 1 3 2

# 9
# 8 7 9 2 5 4 6 3 1
# 8 9 7 5 6 4 1 3 2