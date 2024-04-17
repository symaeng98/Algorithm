from collections import defaultdict

n = int(input())
word = input()
word_list = list(word)
arr = [sorted(list(input())) for _ in range(n-1)]
answer_list = []

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
         "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]

# 더하기
for a in alpha:
    answer_list.append(sorted(list(word+a)))

# 빼기
for i in range(len(word)):
    answer_list.append(sorted(list(word[:i] + word[i+1:])))

# 교체하기
for i in range(len(word)):
    for a in alpha:
        answer_list.append(sorted(list(word[:i] + word[i+1:] + a)))

result = 0
for a in arr:
    if a in answer_list:
        result += 1
print(result)