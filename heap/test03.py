import heapq

def change(heap):
    tmp_heap = []
    new_heap = []
    for i in heap:
        heapq.heappush(tmp_heap,-i)
    heapq.heappop(tmp_heap)
    for i in tmp_heap:
        heapq.heappush(new_heap,-i)
    
    return new_heap       

def solution(operations):
    answer = [0,0]
    h = []
    
    for operation in operations:
        oper,num = operation.split()
        
        if oper == 'I':
            heapq.heappush(h,int(num))
            
        if len(h) >=1:    
            if oper == 'D' and int(num) == -1:
                heapq.heappop(h)
            elif oper == 'D' and int(num) == 1:
                h = change(h)
        else:
            continue
    
    if len(h) > 0:
        answer[0] = max(h)
        answer[1] = min(h)
        
    return answer
