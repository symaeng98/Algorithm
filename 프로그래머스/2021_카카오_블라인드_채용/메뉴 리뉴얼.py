from itertools import combinations
def solution(orders, course):
    menus = {}

    for c in course:
        for order in orders:
            for comb in combinations(order, c):
                tmp = ''.join(sorted(comb))
                if tmp not in menus:
                    menus[tmp] = 0
                menus[tmp] += 1

    sm = sorted(menus.items(), key=lambda x:-x[1])
    result = []
    max_cnt = [0]*20
    for c in course:
        mc = -1
        for menu, cnt in sm:
            if len(menu) != c:
                continue
            mc = max(mc, cnt)
        max_cnt[c] = mc

    for c in course:
        for menu, cnt in sm:
            if len(menu) != c:
                continue

            if 2 <= cnt == max_cnt[c]:
                result.append(menu)
    return sorted(result)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))