def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp

    max_a, max_b = 0, 0
    for a, b in sizes:
        max_a = max(a, max_a)
        max_b = max(b, max_b)

    return max_a*max_b


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]	))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))