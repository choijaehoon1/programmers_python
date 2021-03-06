answer = []
def dfs(tickets, route, visit):
    global answer
    
    if len(route) == len(tickets) + 1:
        answer.append(route)
    else:
        for i in range(len(tickets)):
            if route[-1] == tickets[i][0] and visit[i] == 0:
                new_visit = visit[:]
                new_visit[i] = 1
                dfs(tickets, route + [tickets[i][1]], new_visit)
            
            
def solution(tickets):
    global answer
    visit = [0 for _ in range(len(tickets))]
    dfs(tickets, ['ICN'], visit)
    answer.sort()    
    return answer[0]
