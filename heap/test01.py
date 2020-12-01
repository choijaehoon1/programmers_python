import heapq
def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h,i)
    
    while h:
        if len(h) == 1 and h[0] < K:
            return -1
        
        if len(h) == 1 and h[0] >= K:
            return answer
        
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        
        if a < K:
            num = a + b*2
            heapq.heappush(h,num)
            answer += 1
        else:
            break

    return answer
