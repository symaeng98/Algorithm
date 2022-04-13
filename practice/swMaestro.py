### 1번 ###
# from itertools import combinations as com
# import copy
#
# def customerNum(List, N, M):
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if List[i][j] >= 5:
#                 cnt += 1
#                 break
#     return cnt
#
# N, M, K = map(int, input().split(" "))
# fav = []
# for i in range(N):
#     fav.append(list(map(int, input().split(" "))))
#
# numList = [int(x) for x in range(M)]
# customerNumList = []
#
# for c in com(numList, K):
#     copyNumList = copy.deepcopy(fav)
#     for i in range(N):
#         for j in range(K):
#             copyNumList[i][c[j]] = -1
#     customerNumList.append(customerNum(copyNumList,N,M))
#
# print(max(customerNumList))


### 2번 ###
def dfs(g, sc, v, index, result, resultnum):
    if v[index] == 1:
        return
    v[index] = 1
    if sc[index] > 0:
        result[0] -= sc[index]
        resultnum[0] += 1
    for i in range(len(g[index])):
        dfs(g,sc,v,g[index][i],result,resultnum)
    return




N, M, K = map(int, input().split(" "))
graph = [[] for _ in range(N+1)]
scoreList = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(M):
    ind, score = map(int, input().split(" "))
    scoreList[ind] = score
for i in range(K):
    ind1, ind2 = map(int, input().split(" "))
    graph[ind1].append(ind2)
    graph[ind2].append(ind1)

scoreForDFS = [0]
friendsNum = [0]
for i in range(1,N+1):
    if scoreList[i] == 0:
        dfs(graph,scoreList,visited,i,scoreForDFS,friendsNum)
        scoreList[i] = -(-scoreForDFS[0] // friendsNum[0])

        visited = [0 for _ in range(N+1)]
        scoreForDFS[0] = 0
        friendsNum[0] = 0

for i in range(1,N+1):
    if scoreList[i] < 0:
        scoreList[i] = -scoreList[i]

avg = round(sum(scoreList)/N,3)
avg = format(avg,".2f")
print(avg)