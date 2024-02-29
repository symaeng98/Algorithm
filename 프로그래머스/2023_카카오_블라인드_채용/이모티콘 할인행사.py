from itertools import product

def solution(users, emoticons):
    answer = []
    discount_rates = [0.1, 0.2, 0.3, 0.4]
    for discount_rate in product(discount_rates, repeat=len(emoticons)):
        discount_emoticons = []
        for i in range(len(emoticons)):
            discount_emoticons.append(int((1-discount_rate[i])*100)*emoticons[i]//100)

        plus_num = 0
        total_price = [0]*len(users)
        for i, user in enumerate(users):
            pur_rate, plus_price = user[0], user[1]
            for j in range(len(discount_emoticons)):
                if pur_rate <= discount_rate[j]*100: # 삼
                    total_price[i] += discount_emoticons[j]
            if total_price[i] >= plus_price:
                total_price[i] = 0
                plus_num += 1

        answer.append([plus_num, sum(total_price)])

    return sorted(answer, key=lambda x:(x[0], x[1]), reverse=True)[0]


print(solution([[40, 10000]], [7000, 9000]))
print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))