def solution(lines):
    answer = 0
    def to_ms(x):
        tmp = x.split(":")
        h, m = tmp[0], tmp[1]
        s, ms = tmp[2].split(".")

        return 3600000*int(h) + 60000*int(m) + 1000*int(s) + int(ms)

    result = []
    for line in lines:
        arr = line.split(" ")
        end = to_ms(arr[1])
        start = end - int(1000*float(arr[2][:-1])) + 1
        result.append((start, end))

    for i in range(len(result)):
        head = result[i][1]
        tail = head + 999

        cnt = 0
        for j in range(len(result)):
            if result[j][0] <= tail and result[j][1] >= head:
                cnt += 1

        answer = max(cnt, answer)

    return answer