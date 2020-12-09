def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0: # 제일 왼쪽인 경우
                triangle[i][j] += triangle[i-1][j]
            elif i == j: # 제일 오른쪽인 경우                
                triangle[i][j] += triangle[i-1][j-1]
            else: # 중간인 경우
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
            
    answer = max(triangle[len(triangle)-1])    
    
    return answer
