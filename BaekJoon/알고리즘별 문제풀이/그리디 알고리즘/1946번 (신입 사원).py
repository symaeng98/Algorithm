t = int(input())
for _ in range(t):
    n = int(input())
    score = []
    for _ in range(n):
        a, b = map(int, input().split())
        score.append((a, b))
    score.sort()

    result = 1
    top = 0
    for i in range(1, len(score)):
        if score[top][1] > score[i][1]:
            result += 1
            top = i

    print(result)