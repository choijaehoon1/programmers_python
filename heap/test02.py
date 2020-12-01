import heapq
def solution(jobs):
    answer = 0
    length = len(jobs)
    jobs.sort()
    h = []
    last = -1 # 작업끝난시간
    cnt = 0
    time = jobs[0][0]
    
    total = 0
    
    while cnt < length:
        for s,t in jobs:
            if last < s <= time:
                heapq.heappush(h,(t,s)) # 반대로, 최소힙 이용
        
        if len(h) > 0:
            cnt += 1
            last = time
            term, start = heapq.heappop(h)
            time += term
            answer += (time-start)
        else:
            time += 1
        
    answer //= length
                   
    return answer
