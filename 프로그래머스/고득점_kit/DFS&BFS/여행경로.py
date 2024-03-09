from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    count_dict = defaultdict(int)
    for s, e in tickets:
        graph[s].append(e)
        count_dict[s+e] += 1
    for g in graph:
        graph[g].sort()

    result = []
    def dfs(airport, way, cnt):
        if cnt == 0:
            result_way = way.copy()
            result_way.append(airport)
            result.append(result_way)
        for dest in graph[airport]:
            if count_dict[airport+dest] != 0:
                count_dict[airport+dest] -= 1
                way.append(airport)
                dfs(dest, way, cnt-1)
                way.pop()
                count_dict[airport+dest] += 1
    dfs("ICN", [], len(tickets))

    return sorted(result)[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))