def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    
    check = [0] * len(routes)
    
    for i in range(len(routes)):
        if check[i] == 0:
            camera = routes[i][1]
            answer += 1
        
        for j in range(i+1,len(routes)):
            if routes[j][0] <= camera <= routes[j][1] and check[j] == 0:
                check[j] = 1
    
    return answer
