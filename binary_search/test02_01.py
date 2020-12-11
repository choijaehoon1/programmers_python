from itertools import combinations
def solution(distance, rocks, n):
    answer = 0
    
    for combi in combinations(rocks,n):
        tmp = [i for i in rocks if i not in combi]
        tmp.sort()
        start = 0
        end = distance
        result = []
        for j in tmp:
            a = j - start
            result.append(a)
            start = j
        result.append(end - tmp[-1])
        answer = max(answer,min(result)) 
        
    
    return answer
