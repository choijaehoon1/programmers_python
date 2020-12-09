# 아래로 이동과 오른쪽으로 이동
dx = [1,0]
dy = [0,1]
answer = 0

def dfs(x,y,board,visit,m,n):
    global answer
    
    if x == n and y == m:
        answer += 1
        return

    for k in range(2):
        nx = dx[k] + x
        ny = dy[k] + y
        if 0 <= nx < n+1 and 0 <= ny < m+1:
            if visit[nx][ny] == 0 and board[nx][ny] == 0:
                visit[nx][ny] = -1
                dfs(nx,ny,board,visit,m,n)
                visit[nx][ny] = 0
    
def solution(m, n, puddles):
    global answer
    board = [[0]*(m+1) for _ in range(n+1)] # 한칸 더 여유있게 잡음
    visit = [[0]*(m+1) for _ in range(n+1)]
    for puddle in puddles:
        x,y = puddle # x,y좌표 반대임
        board[y][x] = -1
        visit[y][x] = -1
    
    dfs(1,1,board,visit,m,n) # (1,1)부터 시작이므로
    return answer % 1000000007
