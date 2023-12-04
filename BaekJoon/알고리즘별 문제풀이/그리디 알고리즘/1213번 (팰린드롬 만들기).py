word = input()

alpha_dict = {}

for s in word:
    if s not in alpha_dict:
        alpha_dict[s] = 1
    else:
        alpha_dict[s] += 1

total_odd = 0
middle_s = ""
middle_s_cnt = 0
for s, v in alpha_dict.items():
    if v%2 != 0:
        total_odd += 1
        middle_s = s
        middle_s_cnt = v

if total_odd > 1:
    print("I'm Sorry Hansoo")
else:
    if total_odd == 0:
        sorted_alpha_dict = sorted(alpha_dict.items(), key=lambda x:x[0])
        reversed_alpha_dict = sorted(alpha_dict.items(), key=lambda x:x[0], reverse=True)
        result = ""
        for s, v in sorted_alpha_dict:
            result += s*(v//2)
        for s, v in reversed_alpha_dict:
            result += s*(v//2)
        print(result)
    else:
        if middle_s_cnt == 1:
            del alpha_dict[middle_s]
        else:
            alpha_dict[middle_s] -= 1
        sorted_alpha_dict = sorted(alpha_dict.items(), key=lambda x:x[0])
        reversed_alpha_dict = sorted(alpha_dict.items(), key=lambda x:x[0], reverse=True)
        result = ""
        for s, v in sorted_alpha_dict:
            result += s*(v//2)
        result += middle_s
        for s, v in reversed_alpha_dict:
            result += s*(v//2)
        print(result)
