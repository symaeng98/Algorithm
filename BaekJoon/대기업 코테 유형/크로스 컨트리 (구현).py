from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    team_score_dict = defaultdict(int)
    for i in range(1, max(arr)+1):
        team_cnt = arr.count(i)
        if team_cnt < 6:
            for j in range(len(arr)):
                if arr[j] == i:
                    arr[j] = -1

    team_max_cnt = defaultdict(int)
    point = 1
    score = []
    for i in range(len(arr)):
        if arr[i] != -1:
            if team_max_cnt[arr[i]] >= 4:
                score.append(point)
                point += 1
                continue
            team_score_dict[arr[i]] += point
            score.append(point)
            point += 1
            team_max_cnt[arr[i]] += 1
        else:
            score.append(0)

    fifth_dict = defaultdict(int)
    for team in team_score_dict.keys():
        cnt = 0
        for i in range(len(arr)):
            if arr[i] == team:
                cnt += 1
                if cnt == 5:
                    fifth_dict[team] += score[i]

    winner = -1
    min_fifth = 1e9
    min_score = 1e9
    for team in team_score_dict.keys():
        if min_score > team_score_dict[team]:
            winner = team
            min_fifth = fifth_dict[team]
            min_score = team_score_dict[team]
        elif min_score == team_score_dict[team]:
            if min_fifth > fifth_dict[team]:
                winner = team
                min_fifth = fifth_dict[team]
                min_score = team_score_dict[team]

    print(winner)