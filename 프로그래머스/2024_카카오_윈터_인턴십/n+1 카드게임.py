def solution(coin, cards):
    n = len(cards)
    cost = n+1
    now = cards[:n//3]
    left = cards[n//3:]
    left.reverse()
    picked = []

    result = 1
    while True:
        if not left:
            break
        picked.append(left.pop())
        picked.append(left.pop())

        is_found = False
        for o in now:
            op = cost - o
            if op in now:
                is_found = True
                now.remove(op)
                now.remove(o)
                result += 1
                break
        if is_found:
            continue

        is_found = False
        if coin >= 1:
            for o in now:
                op = cost - o
                if op in picked:
                    picked.remove(op)
                    now.remove(o)
                    result += 1
                    coin -= 1
                    is_found = True
                    break
            if is_found:
                continue

        is_found = False
        if coin >= 2:
            for p in picked:
                op = cost - p
                if op in picked:
                    picked.remove(op)
                    picked.remove(p)
                    result += 1
                    coin -= 2
                    is_found = True
                    break
            if is_found:
                continue

        break

    return result