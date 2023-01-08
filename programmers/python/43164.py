# Lv 3. 여행경로 - 깊이/너비 우선 탐색(DFS/BFS)

import collections

def solution(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    answer = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        answer.append(a)

    dfs('ICN')

    return answer[::-1]

answer = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
print(answer)