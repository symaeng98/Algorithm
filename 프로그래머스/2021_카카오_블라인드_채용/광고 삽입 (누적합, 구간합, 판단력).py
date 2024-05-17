def str_to_int(t):
    h, m, s = t.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def solution(play_time, adv_time, logs):
    answer = ''
    logs_start_sec = []
    logs_end_sec = []
    for log in logs:
        s, e = log.split("-")
        logs_start_sec.append(str_to_int(s))
        logs_end_sec.append(str_to_int(e))


    play_time_sec = str_to_int(play_time)
    adv_time_sec = str_to_int(adv_time)


    total_time = [0]*400000
    for i in range(len(logs)):
        total_time[logs_start_sec[i]] += 1
        total_time[logs_end_sec[i]] -= 1


    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i-1]

    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i-1]


    max_view = -1
    max_time = -1
    for i in range(adv_time_sec - 1, play_time_sec):
        if i >= adv_time_sec:
            if max_view < total_time[i] - total_time[i - adv_time_sec]:
                max_view = total_time[i] - total_time[i - adv_time_sec]
                max_time = i - adv_time_sec + 1
        else:
            if max_view < total_time[i]:
                max_view = max(max_view, total_time[i])
                max_time = i - adv_time_sec + 1

    h = max_time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    max_time = max_time % 3600
    m = max_time // 60
    m = '0' + str(m) if m < 10 else str(m)
    max_time = max_time % 60
    s = '0' + str(max_time) if max_time < 10 else str(max_time)

    return h + ':' + m + ':' + s