def solution(p):
    if len(p) == 0:
        return ""
    u, v = seperate(p)
    if check_right(u):
        s = solution(v)
        return u + s

    tmp = "(" + solution(v) + ")"
    s = remove_and_reverse(u)

    return tmp + s

def seperate(s):
    l_cnt = 0
    r_cnt = 0
    for i in range(len(s)):
        if l_cnt != 0 and r_cnt != 0:
            if l_cnt == r_cnt:
                return (s[:i], s[i:])
        if s[i] == "(":
            l_cnt += 1
        else:
            r_cnt += 1
    return (s,"")


def check_right(s):
    tmp = [s[0]]
    for i in range(1, len(s)):
        if (tmp[-1] == "(" and s[i] == ")"):
            tmp.pop()
        else:
            tmp.append(s[i])
    if len(tmp) != 0:
        return False
    else:
        return True

def remove_and_reverse(u):
    tmp = ""
    u = u[1:-1]
    for i in range(len(u)):
        if u[i] == "(":
            tmp += ")"
        else:
            tmp += "("
    return tmp
