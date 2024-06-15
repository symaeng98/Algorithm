def solution(n, stations, w):
    def get_station_count(k):
        l = w*2+1
        if k%l == 0:
            return k//l
        return k//l+1

    range_list = []
    for station in stations:
        range_list.append((station-w, station+w))

    empty = []
    start = 1
    for left, right in range_list:
        empty.append((start, left-1))
        start = right+1
    empty.append((start, n))

    result = 0
    for left, right in empty:
        if left > right:
            continue
        result += get_station_count(right-left+1)
    return result