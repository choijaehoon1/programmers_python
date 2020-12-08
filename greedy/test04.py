from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    light = 0
    heavy = len(people) - 1
    
    cnt = 0 
    while light < heavy:
        if people[light] + people[heavy] <= limit: # 동승할 수 있는 경우
            cnt += 1
            light += 1
            heavy -= 1
        else:
            heavy -= 1
    # print(cnt)
    answer = len(people) - cnt
    return answer
