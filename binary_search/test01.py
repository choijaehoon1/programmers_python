def solution(n, times):
    answer = 0
    
    start = 0
    end = max(times)*n # 최악의 경우(심사 가장 오래걸리는 사람한테 모두 다 받는 경우)
    
    while start <= end:
        mid = (start + end) // 2 # 심사받는데 걸리는 시간
        people = 0 # 인원 수
        for i in times: 
            people += mid // i # 각 심사관한테 받을 수 있는 심사인원으 수
            # 모든 사람을 심사할 수 있으면 빠져나옴
            if people >= n: 
                break
        
        if people >= n: # 심사를 더 많이한 경우 시간을 줄여봄
            answer = mid
            end = mid - 1
        else:
            start = mid + 1 
        
    return answer
