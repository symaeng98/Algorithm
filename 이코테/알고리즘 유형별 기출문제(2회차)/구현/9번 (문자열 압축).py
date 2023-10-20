def solution(s):
    answer = 0
    result = 1e9
    for i in range(1, len(s)+1):
        result = min(result, cnt_word(s, i))
    return result

def cnt_word(s, length):
    arr = []
    index = 0
    result = 0
    cnt = 0
    word = s[:length]
    while True:
        if word == s[index:index+length]:
            index += length
            cnt += 1
        else:
            if cnt == 1:
                result += length
            else:
                result += len(str(cnt)) + length
            cnt = 0
            word = s[index:index+length]

        if index >= len(s):
            if cnt == 1:
                result += len(word)
            else:
                result += len(str(cnt)) + len(word)
            break

    return result