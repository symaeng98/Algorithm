INF = 1e9
t = int(input())
for _ in range(t):
    w = input()
    k = int(input())
    s_list = list(set(list(w)))

    min_value = INF
    max_value = -1
    for s in s_list: # 26
        index = []
        for i in range(len(w)):
            if w[i] == s:
                index.append(i)

        tmp_min = INF
        tmp_max = -1
        for i in range(len(index)):
            if i+k-1 >= len(index):
                break
            tmp_min = min(tmp_min, index[i+k-1] - index[i] + 1)
            tmp_max = max(tmp_max, index[i+k-1] - index[i] + 1)

        min_value = min(min_value, tmp_min)
        max_value = max(max_value, tmp_max)

    if min_value == INF or max_value == -1:
        print(-1)
    else:
        print(min_value, max_value)

