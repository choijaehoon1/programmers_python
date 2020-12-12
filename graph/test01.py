from collections import deque

def bfs(v,visit,graph):
    q = deque()
    cnt = 0
    q.append((v,cnt))

    while q:
        v, cnt = q.popleft()
        if visit[v] == -1:
            visit[v] = cnt
            cnt += 1
            for i in graph[v]:
                q.append((i,cnt))
    
def solution(n, edge):
    answer = 0
    visit = [-1 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for i in edge:
        a,b = i
        graph[a].append(b)
        graph[b].append(a)

    bfs(1,visit,graph)
    # print(visit)
    answer = visit.count(max(visit))
    
    return answer
