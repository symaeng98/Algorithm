n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]

answer = -1
for i in range(n):
    sushi_list = []
    for j in range(k):
        sushi_list.append(belt[(i+j)%n])
    sushi_list.append(c)
    result = len(set(sushi_list))
    if answer < result:
        answer = result

print(answer)