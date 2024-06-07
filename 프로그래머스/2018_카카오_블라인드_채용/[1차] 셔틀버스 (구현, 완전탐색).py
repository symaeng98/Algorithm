import copy
from collections import defaultdict
def solution(n, t, m, timetable):
    def to_minute(s):
        h, m = s.split(":")
        return 60*int(h) + int(m)
    def to_str(minute):
        h, m = str(minute//60), str(minute%60)
        if len(h) == 1:
            h = "0"+h
        if len(m) == 1:
            m = "0"+m
        return h+":"+m

    def get_bus_table():
        start = 540
        result = []
        for i in range(n):
            result.append(start + t*i)
        return result
    bus_table = get_bus_table()
    wait_table = []
    for tt in timetable:
        wait_table.append(to_minute(tt))

    result = []
    for now in range(1440):
        wait_table_tmp = copy.deepcopy(wait_table)
        wait_table_tmp.append(now)
        wait_table_tmp.sort()
        index = 0
        result_dict = defaultdict(list)
        for eta in bus_table:
            member = 0
            for i in range(index, len(wait_table_tmp)):
                if member < m and wait_table_tmp[i] <= eta:
                    member += 1
                    result_dict[eta].append(wait_table_tmp[i])
                else:
                    index = i
                    break

        now_cnt = wait_table.count(now)+1
        cnt = 0
        for value_list in result_dict.values():
            for value in value_list:
                if value == now:
                    cnt += 1
        if now_cnt == cnt:
            result.append(now)
        else:
            break

    return to_str(result[-1])