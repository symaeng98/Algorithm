from collections import defaultdict

n, m = map(int, input().split())
word_cnt_dict = defaultdict(int)
word_list = []
for _ in range(n):
    word = input()
    if len(word) < m:
        continue
    if word_cnt_dict[word] == 0:
        word_list.append(word)
    word_cnt_dict[word] += 1

result = sorted(word_list, key= lambda x:(-word_cnt_dict[x], -len(x), x))

for res in result:
    print(res)