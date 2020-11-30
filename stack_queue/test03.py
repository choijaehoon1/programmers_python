from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    for i in truck_weights:
        q.append(i)
    
    tmp_q = deque([0]* bridge_length)
    
    time = 0
    on_weight = 0
    while q:
        time += 1
        
        on_weight -= tmp_q.popleft()
        if (on_weight + q[0]) <= weight:
            now = q.popleft()
            on_weight += now
            tmp_q.append(now)
        else:
            tmp_q.append(0) # 안되니까 그냥 0을 더하는 것
    
    # 지난 시간에 다리의 길이만큼 더해줘야 정답
    answer = time + bridge_length
        
    return answer
