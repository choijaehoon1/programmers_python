from collections import deque
def solution(priorities, location):
    q = deque()
    result = []
    end = -1e9
    for i in range(len(priorities)):
        q.append((priorities[i],i))
        if end < priorities[i]:
            end = priorities[i]
            
    while q:
        now,locate = q.popleft()
        if len(q) == 0:
            max_value = 0
        else:
            max_value = max(q)[0]
        if now < max_value:
            q.append((now,locate))
        else:
            result.append((now,locate))
    
    answer = 1
    for i in result:
        if location == i[1]:
            break
        answer += 1    
    
    return answer
