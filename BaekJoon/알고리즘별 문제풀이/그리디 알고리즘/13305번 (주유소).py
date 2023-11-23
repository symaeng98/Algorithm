n = int(input())
distance = list(map(int, input().split()))
costs = list(map(int, input().split()))

now_cost = costs[0]
length = 0
total = 0
for i in range(1, len(costs)):
    if now_cost > costs[i] or i == len(costs)-1:
        length += distance[i-1]
        total += length*now_cost
        length = 0
        now_cost = costs[i]
    else:
        length += distance[i-1]

print(total)