def solution(s):
    minLength = 10000
    for i in range(1, len(s)+1):
        startIndex = 0
        length = i
        lengthSum = 0
        while(startIndex < len(s)):
            result, sInd = check(s, startIndex, length)
            lengthSum += len(result)
            startIndex = sInd
        if minLength > lengthSum:
            minLength = lengthSum
    return minLength


def check(s, startIndex, length):
    word = s[startIndex:startIndex+length]

    cnt = 0
    sInd = startIndex
    while(sInd < len(s)):
        if word == s[sInd:sInd+length]:
            cnt += 1
            sInd += length
        else:
            break
    if cnt == 1:
        return (word, sInd)
    return (str(cnt)+word, sInd)
