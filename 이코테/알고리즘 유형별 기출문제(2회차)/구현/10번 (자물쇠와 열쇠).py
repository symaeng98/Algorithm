def solution(key, lock):
    n = len(lock)
    m = len(key)
    ex_lock = [[0]*(n*3) for _ in range((n*3))]
    for i in range(n):
        for j in range(n):
            ex_lock[i+n][j+n] = lock[i][j]



    for i in range(4):
        for j in range(n*2+1):
            for k in range(n*2+1):
                for l in range(m):
                    for o in range(m):
                        ex_lock[j+l][k+o] += key[l][o]
                if check(ex_lock) == True:
                    return True
                for l in range(m):
                    for o in range(m):
                        ex_lock[j+l][k+o] -= key[l][o]
        rotate(key)

    return False

def check(ex_lock):
    n = len(ex_lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if ex_lock[i][j] != 1:
                return False
    return True


def rotate(key):
    m = len(key)
    tmp = [[0]*m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            tmp[i][j] = key[m-1-j][i]

    for i in range(m):
        for j in range(m):
            key[i][j] = tmp[i][j]

