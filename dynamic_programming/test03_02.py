def solution(m, n, puddles):
    answer = [[0]*(m+1) for _ in range(n+1)]
    
    answer[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1: # 시작 위치일때는 무시
                continue
            if [j,i] in puddles: # 웅덩이 일때는 0으로 값 변환 
                answer[i][j] = 0
            else: # 위의값과 왼쪽값을 더해줌
                answer[i][j] = (answer[i-1][j] + answer[i][j-1]) 
    
    return answer[n][m] % 1000000007
