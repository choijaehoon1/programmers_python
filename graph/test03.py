from collections import deque

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def solution(arrows):
    answer = 0
    q = deque()
    v = {} # 정점
    dir = {} # 경로
    
    # 초기 설정
    x,y = 0,0
    q.append((x,y))
    v[(x,y)] = 0
    
    # arrows에서 정점, 방향 정보를 저장
    for i in arrows:
        for j in range(2): # 교차될수도 있으니 거리를 2배로 잡고 수행
            nx = x + dx[i]
            ny = y + dy[i]
            q.append((nx,ny))
            v[(nx,ny)] = 0
            # 반대로 돌아가는 경로 고려
            dir[(x,y,nx,ny)] = 0 
            dir[(nx,ny,x,y)] = 0
            x,y = nx,ny    
    
    x,y = q.popleft()
    v[(x,y)] = 1
    
    while q:
        nx, ny = q.popleft()
        if v[(nx,ny)] == 1 and dir[(x,y,nx,ny)] == 0: # 정점을 들린적이 있는데 경로는 새로운 경로일 때 사이클 생성됨
            answer += 1
            dir[(x,y,nx,ny)] = 1
            dir[(nx,ny,x,y)] = 1
        else: # 해당 위치 방문 처리 및 경로 방문 처리
            v[(nx,ny)] = 1
            dir[(x,y,nx,ny)] = 1
            dir[(nx,ny,x,y)] = 1
        x,y = nx,ny
    
    return answer
