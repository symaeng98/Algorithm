from itertools import product
def solution(word):
    arr = ["A", "E", "I", "O", "U"]
    answer_arr = []
    for i in range(1, 6):
        for p in product(arr, repeat=i):
            answer_arr.append(''.join(p))

    answer_arr.sort()

    for i in range(len(answer_arr)):
        if word == answer_arr[i]:
            return i+1

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))