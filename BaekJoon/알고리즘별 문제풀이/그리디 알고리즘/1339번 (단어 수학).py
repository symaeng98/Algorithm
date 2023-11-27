n = int(input())
words = []
alpha_dict = {}
for _ in range(n):
    words.append(input())

for word in words:
    for i in range(len(word)):
        if word[i] not in alpha_dict.keys():
            alpha_dict[word[i]] = 10 ** (len(word) - 1 - i)
        else:
            alpha_dict[word[i]] += 10 ** (len(word) - 1 - i)

sorted_alpha_dict = sorted(alpha_dict.items(), key=lambda x: x[1], reverse=True)

alpha_num_dict = {}

num = 9
for alpha in sorted_alpha_dict:
    alpha_num_dict[alpha[0]] = num
    num -= 1

num_list = []
for word in words:
    num = ""
    for alpha in word:
        num += str(alpha_num_dict[alpha])

    num_list.append(int(num))

print(sum(num_list))