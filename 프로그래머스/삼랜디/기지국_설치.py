# 9:00 ~ 9:21
def solution(n, stations, w):
    answer = 0
    blanks = []
    bl_start = 1
    for station in stations:
        st_start = station-w
        st_end = station+w
        if st_start <= bl_start <= st_end:
            bl_start = st_end+1
            continue
        blanks.append((bl_start, st_start-1))
        bl_start = st_end+1
    if bl_start <= n:
        blanks.append((bl_start, n))

    for s, e in blanks:
        answer += (e-s+1) // (2*w+1)
        if (e-s+1) % (2*w+1) == 0:
            continue
        answer += 1
    return answer