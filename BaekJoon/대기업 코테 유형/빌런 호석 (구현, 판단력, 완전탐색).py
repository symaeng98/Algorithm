n, k, p, x = map(int, input().split())
# k자리
# 현재 x
# p개 반전
bulbs = [[1,1,1,1,1,1,0],
         [0,0,1,1,0,0,0],
         [0,1,1,0,1,1,1],
         [0,1,1,1,1,0,1],
         [1,0,1,1,0,0,1],
         [1,1,0,1,1,0,1],
         [1,1,0,1,1,1,1],
         [0,1,1,1,0,0,0],
         [1,1,1,1,1,1,1],
         [1,1,1,1,1,0,1]
         ]

def switch_count(a, b):
    cnt = 0
    for i in range(7):
        if bulbs[a][i] != bulbs[b][i]:
            cnt += 1
    return cnt


def count(a, b):
    st_a = str(a)
    st_b = str(b)
    len_a = len(st_a)
    len_b = len(st_b)
    if len_a > len_b:
        st_b = "0"*(len_a-len_b)+str(b)
    else:
        st_a = "0"*(len_b-len_a)+str(a)

    # a -> b
    cnt = 0
    length = len(st_a)
    for i in range(length):
        cnt += switch_count(int(st_a[i]), int(st_b[i]))
    return cnt


cnt = 0
for num in range(1, n+1):
    if p >= count(x, num):
        cnt += 1

print(cnt-1)