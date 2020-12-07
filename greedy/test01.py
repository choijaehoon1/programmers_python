def solution(n, lost, reserve):
    answer = 0
    array = [True] * (n+2)
    lost.sort()
    reserve.sort()
    
    # 빌려줄 수 있는 데 자신의 것을 도둑 맞은 경우 테스트 케이스에서 제외 시킴
    for i in reserve:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
    
    for i in lost:
        array[i] = False
    
    for i in range(len(reserve)):
        if array[reserve[i]] == False:
            array[reserve[i]] = True
            continue
        if array[reserve[i]-1] == False:
            array[reserve[i]-1] = True
            continue
        if array[reserve[i]+1] == False:
            array[reserve[i]+1] = True
            continue
    
    for i in range(1,n+1):
        if array[i] == True:
            answer+=1
        
    
    return answer
