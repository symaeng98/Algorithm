def solution(key, lock):
    lockLength = len(lock)
    keyLength = len(key)
    expandedLock = [[0]*(lockLength*3) for _ in range((lockLength*3))]
    for i in range(lockLength):
        for j in range(lockLength):
            expandedLock[i+lockLength][j+lockLength] = lock[i][j]
    # print(expandedLock)


    for i in range(4):
        for j in range(lockLength*2+1):
            for k in range(lockLength*2+1):
                for l in range(keyLength):
                    for m in range(keyLength):
                        expandedLock[j+l][k+m] += key[l][m]
                if check(expandedLock) == True:
                    return True
                for l in range(keyLength):
                    for m in range(keyLength):
                        expandedLock[j+l][k+m] -= key[l][m]
        rotate(key)

    return False

def check(expandedLock):
    length = len(expandedLock) // 3
    for i in range(length, length*2):
        for j in range(length, length*2):
            if expandedLock[i][j] != 1:
                return False
    return True



def rotate(key):
    tmp = [[0]*len(key) for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(key)):
            tmp[i][j] = key[len(key)-1-j][i]

    for i in range(len(key)):
        for j in range(len(key)):
            key[i][j] = tmp[i][j]

