def dfs(n, computers,i,visit):
    if visit[i] == 0:
        visit[i] = 1
    
    for j in range(len(computers)):
        if computers[i][j] == 1 and visit[j] == 0:
            dfs(n, computers,j,visit)
    
def solution(n, computers):
    answer = 0
    visit = [0 for i in range(n)]
    for i in range(len(computers)):
        if visit[i] == 0:
            dfs(n, computers, i, visit)
            answer+=1
                
    return answer
