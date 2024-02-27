def solution(enroll, referral, seller, amount):
    name_dict = {"center": 0}
    for i in range(len(enroll)):
        name_dict[enroll[i]] = i+1
    parent = [0]*(len(enroll)+1)
    for i in range(len(referral)):
        if referral[i] == "-":
            continue
        parent[name_dict[enroll[i]]] = name_dict[referral[i]]

    total_money = [0]*(len(enroll)+1)
    for i in range(len(seller)):
        name = seller[i]
        money = amount[i]*100

        now = name_dict[name]
        while True:
            if now == 0 or money == 0:
                break
            p = parent[now]
            pm = money//10
            m = money - pm
            total_money[now] += m
            money = pm

            now = p
    return total_money[1:]


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))
