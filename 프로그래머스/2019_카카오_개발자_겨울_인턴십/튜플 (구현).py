def solution(s):
    answer = []
    arr = []
    for x in s[2:-2].split("},{"):
        arr.append(list(map(int, x.split(","))))

    arr.sort(key=lambda x:len(x))

    result = [arr[0][0]]
    for i in range(1, len(arr)):
        for k in arr[i]:
            if k not in result:
                result.append(k)
                break

    return result