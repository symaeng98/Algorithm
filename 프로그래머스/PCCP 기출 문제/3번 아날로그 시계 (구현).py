def solution(h1, m1, s1, h2, m2, s2):
    def get_times(h, m, s):

        sd = (s * 6) % 360
        md = (m * 6 + s * 0.1) % 360
        hd = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360

        result = 0
        if sd >= md:
            result += 1
        if sd >= hd:
            result += 1

        result += (h*60 + m)*2
        result -= h
        if h >= 12:
            result -= 2

        result -= 1

        return result

    ans = get_times(h2, m2, s2) - get_times(h1, m1, s1)

    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        ans += 1

    return ans