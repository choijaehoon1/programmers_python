def solution(name):
    answer = 0
    name = list(name)
    base = ['A'] * len(name)
    idx = 0
    
    while True:
        left_idx = 1
        right_idx = 1
        if name[idx] != 'A':
            if ord(name[idx]) - ord('A') > 13: # 아래방향키로 이동하는게 더 최소값이라면
                answer += 26 - (ord(name[idx]) - ord('A'))
            else:
                answer += ord(name[idx]) - ord('A')
            name[idx] = 'A'
            
        # 종료조건    
        if name == base:
            break
        
        # 위치 이동 횟수(오른쪽 또는 왼쪽)
        # 오른쪽이나 왼쪽에 A가 있는 경우(인덱스가 같은 경우는 나올 수 있으나 왼쪽인덱스가 더 커지는 경우는 x)
        for i in range(1,len(name)):
            if name[idx+i] == 'A':
                right_idx += 1
            else:
                break
            if name[idx-i] == 'A':
                left_idx += 1
            else:
                break
                
        # 더 작은 비용를 더해주는것
        if right_idx > left_idx: # 오른쪽 비용이 더크니 왼쪽인덱스 비용을 더해주고 왼쪽인덱스는 빼줌
            answer += left_idx
            idx -= left_idx
        else: # 두 인덱스가 같은 경우는 인덱스를 증가시켜(1) 다음 문자확인
            answer += right_idx
            idx += right_idx
        
    return answer

