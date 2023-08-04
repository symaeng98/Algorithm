N = int(input())

score = [list(input().split()) for _ in range(N)]

scoreDict = {}
for i in range(N):
    k, e, m = map(int, score[i][1:])
    scoreDict[score[i][0]] = [k, e, m]

sortedList = sorted(scoreDict.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))
for l in sortedList:
    print(l[0])