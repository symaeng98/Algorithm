import sys

input = sys.stdin.readline

n, k = map(int, input().split())
segment_tree = [0]*3000000
arr = [1]*n

def build_tree(x, start, end):
    if start == end:
        segment_tree[x] = arr[start]
        return segment_tree[x]
    mid = (start + end) // 2
    segment_tree[x] = build_tree(x*2, start, mid) + build_tree(x*2+1, mid+1, end)
    return segment_tree[x]

build_tree(1, 0, n-1)


def query_sum(x, start, end, order):
    if start == end:
        return start

    mid = (start + end) // 2
    if order <= segment_tree[x*2]:
        return query_sum(x*2, start, mid, order)
    else:
        return query_sum(x*2+1, mid+1, end, order-segment_tree[x*2])


def update(x, start, end, index, value):
    if start > index or index > end:
        return segment_tree[x]
    segment_tree[x] += value
    if start != end:
        mid = (start + end) // 2
        update(x*2, start, mid, index, value)
        update(x*2+1, mid+1, end, index, value)


result = []
ind = 0
size = n
for i in range(n):
    ind = (ind + k-1) % size
    num = query_sum(1, 1, n, ind+1)

    update(1, 0, n-1, num-1, -1)

    result.append(str(num))
    size -= 1

print("<" + ", ".join(result) + ">")