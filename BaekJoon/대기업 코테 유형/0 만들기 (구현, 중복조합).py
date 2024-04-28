from itertools import product

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [str(i) for i in range(1, n+1)]
    cal = ["+", "-", " "]

    result = []
    for p in product(cal, repeat=n-1):
        quest = []
        for i in range(n-1):
            quest.append(arr[i])
            quest.append(p[i])
        quest.append(arr[-1])

        def is_zero(q):
            tmp = []
            index = 0
            while index < len(q):
                if q[index] in ["+", "-"]:
                    tmp.append(q[index])
                    index += 1
                    continue
                if q[index] != " ":
                    s = ""
                    while index < len(q):
                        if q[index] in ["+", "-"]:
                            break
                        if q[index] != " ":
                            s += q[index]
                        index += 1
                    if s != "":
                        tmp.append(s)

            result = int(tmp[0])
            for i in range(1, len(tmp)-1, 2):
                if tmp[i] == "+":
                    result += int(tmp[i+1])
                else:
                    result -= int(tmp[i+1])

            if result == 0:
                return True
            return False

        if is_zero(quest):
            result.append(quest)

    result.sort()
    for r in result:
        print(''.join(r))

    print()