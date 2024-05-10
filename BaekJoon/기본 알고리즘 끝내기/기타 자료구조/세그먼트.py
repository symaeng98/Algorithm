n, k = map(int, input().split())
segment_tree = [0]*2**(int(n**0.5)+1+1)
arr = [1]*n

def build_tree(x, start, end):
    if start == end:
        segment_tree[x] = arr[start]
        return segment_tree[x]
    mid = (start + end) // 2
    segment_tree[x] = build_tree(x*2, start, mid) + build_tree(x*2+1, mid+1, end)
    return segment_tree[x]

build_tree(1, 0, n-1)


def query_sum(x, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[x]

    mid = (start + end) // 2
    return query_sum(x*2, start, mid, left, right) + query_sum(x*2+1, mid+1, end, left, right)


def update(x, start, end, index, value):
    if start > index or index > end:
        return segment_tree[x]
    segment_tree[x] += value
    if start != end:
        mid = (start + end) // 2
        update(x*2, start, mid, index, value)
        update(x*2+1, mid+1, end, index, value)
