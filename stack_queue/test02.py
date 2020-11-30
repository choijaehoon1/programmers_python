from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    for _ in range(len(progresses)):
        q.append(0)
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            q[i] = (100 - progresses[i]) // speeds[i]
        else:    
            q[i] = (100 - progresses[i]) // speeds[i] + 1
    
    while q:
        if len(q) == 1:
            answer.append(1)
            break
        
        now = q.popleft()
        tmp = 1
        for i in range(len(q)):
            if now < q[i]:
                break
            else:
                tmp += 1
        answer.append(tmp)
        if tmp > 1:
            for _ in range(tmp-1):
                q.popleft()
    
    return answer
