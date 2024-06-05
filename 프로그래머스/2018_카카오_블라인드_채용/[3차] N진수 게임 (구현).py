def solution(n, t, m, p):
    def to_n(k):
        if k == 0:
            return ['0']
        result = []
        while k != 0:
            x = k % n
            if x >= 10:
                result.append(chr(55+x))
            else:
                result.append(str(x))
            k //= n
        result.reverse()

        return result

    now = []
    index = 0
    while len(now) < t*m:
        res = to_n(index)
        now.extend(res)
        index += 1

    answer = []
    for i in range(len(now)):
        if i%m == p-1:
            answer.append(now[i])

    return ''.join(answer[:t])