def solution(a, b, g, s, w, t):
    def is_valid(k):
        gold = 0
        silver = 0
        total = 0
        for i in range(len(g)):
            move_cnt = k // (t[i] * 2)

            if k % (t[i] * 2) >= t[i]:
                move_cnt += 1

            if g[i] < move_cnt*w[i]:
                gold += g[i]
            else:
                gold += move_cnt*w[i]

            if s[i] < move_cnt*w[i]:
                silver += s[i]
            else:
                silver += move_cnt*w[i]

            if g[i]+s[i] < move_cnt*w[i]:
                total += g[i]+s[i]
            else:
                total += move_cnt*w[i]

        if gold >= a and silver >= b and total >= a + b:
            return True
        return False

    l = 10**14*4
    start = 0
    end = l
    while start+1 < end:
        mid = (start + end) // 2
        if is_valid(mid):
            end = mid
        else:
            start = mid
    if is_valid(start):
        return start
    else:
        return end