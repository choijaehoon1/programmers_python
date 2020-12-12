def solution(n, results):
    answer = 0
    INF = int(1e9)
    graph = [[INF] *(n+1) for _ in range(n+1)]
    
    for result in results:
        a,b = result
        graph[a][b] = 1
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                graph[i][j] = 0
        
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    # 한 사람씩 확인해가며 게임을 해봤는지 확인
    array = [True] *(n+1)
    for i in range(1,n+1): # 한사람씩
        for j in range(1,n+1): # 다른 사람과 게임했는지 확인
            if i == j: # 같을때는 무시
                continue
            if graph[i][j] == INF and graph[j][i] == INF: # 경로가 존재하지 않으면 게임을 하지 않은 것
                array[i] = False
                break
    # print(array)                
    for i in range(1,len(array)): # 게임을 했던 사람의 수만 구함
        if array[i] == True:
            answer+=1
    
    return answer
