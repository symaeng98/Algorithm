# 9:00
def solution(n, stations, w):
    answer = 0
    blanks = []
    bl_start = 1
    for station in stations:
        st_start = station-w
        st_end = station+w
        blanks.append((bl_start, st_start-1))
        bl_start = st_end+1
    blanks.append((bl_start, n))
    print(blanks)
    for s, e in blanks:
        if s > e:
            continue
        answer += (e-s+1) // (2*w+1)
        if (e-s+1) % (2*w+1) == 0:
            continue
        answer += 1
    return answer