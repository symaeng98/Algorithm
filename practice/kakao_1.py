friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

friends_dic = {}
length = len(friends)
for i in range(length):
    friends_dic[friends[i]] = i

gift_arr = [[0] * length for _ in range(length)]

for gift in gifts:
    from_friend, to_friend = gift.split(" ")
    gift_arr[friends_dic[from_friend]][friends_dic[to_friend]] += 1

gift_give = []
gift_receive = []
for i in range(length):
    gift_give.append(sum(gift_arr[i]))
for i in range(length):
    sum_value = 0
    for j in range(length):
        sum_value += gift_arr[j][i]
    gift_receive.append(sum_value)

gift_point = []
for i in range(length):
    gift_point.append(gift_give[i]-gift_receive[i])

gift_result = [0]*length

for from_friend in range(length):
    for to_friend in range(length):
        if from_friend == to_friend:
            continue
        if gift_arr[from_friend][to_friend] > gift_arr[to_friend][from_friend]: # 더 많이 줬으면
            gift_result[from_friend] += 1
        elif gift_arr[from_friend][to_friend] == gift_arr[to_friend][from_friend]: # 서로 같은 개수의 선물 혹은 주고 받지 않았다면
            if gift_point[from_friend] > gift_point[to_friend]:
                gift_result[from_friend] += 1
        else:
            continue
print(gift_result)



