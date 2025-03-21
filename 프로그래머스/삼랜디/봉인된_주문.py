
def get_10_from_26(n26):
    result = 0
    power = 1
    for i in range(len(n26)-1,-1,-1):
        result += int(ord(n26[i]) - 96) * power
        power *= 26
    return result


def get_26_from_10(n10):
    result = []
    power = 26

    while n10 // power > 0:
        quotient = n10 // power
        reminder = n10 % power
        n10 = quotient
        if reminder == 0:
            result.append('z')
            n10 -= 1
        else:
            result.append(chr(reminder + 96))

    result.append(chr(n10 + 96))
    result.reverse()
    return ''.join(result)


def solution(n, bans):
    answer = ''

    bans_to_10 = []
    for b in bans:
        bans_to_10.append(get_10_from_26(b))
    bans_to_10.sort()

    for i in range(len(bans_to_10)):
        if bans_to_10[i] <= n:
            n += 1
        else:
            break

    return get_26_from_10(n)