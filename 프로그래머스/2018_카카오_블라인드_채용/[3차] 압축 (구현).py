def solution(msg):
    dictionary = [chr(i) for i in range(65, 91)]
    dictionary.insert(0, "")

    result = []
    index = 0
    while index < len(msg):
        tmp = msg[index]
        while True:
            if tmp in dictionary:
                res = dictionary.index(tmp)
                index += 1
                if index == len(msg):
                    result.append(res)
                    return result
                tmp += msg[index]
            else:
                dictionary.append(tmp)
                result.append(res)
                break