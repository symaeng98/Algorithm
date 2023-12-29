def is_pal(w, m):
    if m == 1:
        return True
    if m%2 == 0:
        if is_reversed(w[:m//2], w[m//2:]):
            return True
    else:
        if is_reversed(w[:m//2], w[m//2+1:]):
            return True
    return False


def is_reversed(w1, w2):
    length = len(w1)
    for i in range(length):
        if w1[i] != w2[length-i-1]:
            return False
    return True


t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    words = list(input() for _ in range(n))
    used = [False]*n

    cnt = 0
    for i in range(n):
        if used[i]:
            continue
        for j in range(i+1, n):
            if is_reversed(words[i], words[j]):
                cnt += 2*m
                used[i] = True
                used[j] = True

    for i in range(n):
        if not used[i]:
            if is_pal(words[i], m):
                cnt += m
                break
    print(f"#{test_case} {cnt}")
