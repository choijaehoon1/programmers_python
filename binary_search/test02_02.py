def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    start = 0
    end = distance
    
    while start <= end:
        mid = (start + end) // 2 # 바위 사이의 최소 거리
        prev = 0 # 반복할때마다 처음 이전돌은 시작위치인 0으로 설정
        remove_rock = 0
        min_value = int(1e9)
        
        for i in range(len(rocks)):
            if rocks[i] - prev < mid: # 현재바위와 이전 돌위치사이의 거리가 최소거리보다 값이 작을때
                remove_rock += 1
            else:
                min_value = min(min_value, rocks[i] - prev) # 바위 사이의 거리가 가장 작은 값으로 갱신
                prev = rocks[i] # 이전 돌위치 갱신
        
        if remove_rock > n: # 삭제된 돌이 더 많은경우 거리를 줄임
            end = mid - 1
        else:
            answer = min_value
            start = mid + 1
        
    return answer
