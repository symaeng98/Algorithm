def check(s):
    length = len(s)
    if length == 1:
        return True

    mid = length // 2
    if s[mid] == "0":
        if "1" in s:
            return False
        return True

    return check(s[:mid]) and check(s[mid+1:])

def solution(numbers):
    answer = []
    for number in numbers:
        bi_num = bin(number)[2:]
        length = len(bi_num)
        for i in range(1, 50):
            if length == 2**i-1:
                break
            if length < 2**i-1:
                bi_num = "0"*((2**i-1)-length) + bi_num
                break

        if check(bi_num):
            answer.append(1)
        else:
            answer.append(0)
    return answer

# print(solution([7, 42, 5]))
# print(solution([63, 111, 95]))
print(solution([1, 2, 21, 128, 14]))