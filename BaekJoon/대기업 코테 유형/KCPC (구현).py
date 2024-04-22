# id, num, rtime

# 점수,횟수,시간
from collections import defaultdict

x = int(input())
for _ in range(x):
    n, k, t, m = map(int, input().split())
    # t보다 점수가 높은 것의 개수 + 1

    team_score = [[-1]*(k+1) for _ in range(n+1)]


    submit_time_rank = []
    cnt_dict = defaultdict(int)
    for _ in range(m):
        team_id, p_num, score = map(int, input().split())
        if team_id in submit_time_rank:
            submit_time_rank.remove(team_id)
        submit_time_rank.append(team_id)

        if team_score[team_id][p_num] < score:
            team_score[team_id][p_num] = score

        cnt_dict[team_id] += 1

    submit_time_rank_dict = defaultdict(int)
    for i in range(n):
        submit_time_rank_dict[submit_time_rank[i]] = i

    team_score_dict = defaultdict(int)
    for i in range(1, n+1):
        for sc in team_score[i]:
            if sc != -1:
                team_score_dict[i] += sc

    teams = [i for i in range(1, n+1)]
    rank = sorted(teams, key=lambda x:(-team_score_dict[x], cnt_dict[x], submit_time_rank_dict[x]))
    for i in range(n):
        if rank[i] == t:
            print(i+1)
            break