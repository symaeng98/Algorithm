n = int(input())
homeworks = []
for _ in range(n):
    d, w = map(int, input().split())
    homeworks.append([w, d])

homeworks.sort(reverse=True)

day = 0
result = [0]*1001
for score, left_day in homeworks:
    for i in range(left_day, -1, -1):
        if result[i] == 0:
            result[i] = score
            break
print(sum(result[1:]))
