def solution(N, number):
    answer = 0
    possible = [0,[N]] # i_half에서 첫번째 인덱스 부터 사용하므로 0을 넣어주고 처음 숫자 넣어줌
    
    if N == number: # N으로 number를 바로 만들 수 있으면 리턴 1 
        return 1
    
    for i in range(2,9): # 2부터 8까지만 확인, 최소값이 8보다 크면 -1 리턴
        case = [] # 임시 리스트
        base_num = int(str(N)*i) # 반복문 돌때마다 하나씩 숫자를 더 넣어줌
        case.append(base_num) 
        for i_half in range(1,i//2+1): # 절반 까지만 검사하면 됨(절반 이상넘어가면 똑같은거 반복임 ex) 1,3과 3,1)
            # x+y가 i가 되도록 만들어 준 것
            for x in possible[i_half]: 
                for y in possible[i-i_half]: 
                    case.append(x+y)
                    case.append(x-y)
                    case.append(y-x)
                    case.append(x*y)
                    if x != 0:
                        case.append(y/x)
                    if y != 0:
                        case.append(x/y)    
                        
        if number in case: # 만족할 때의 횟수는 i이므로 리턴
            return i
        possible.append(case) # 다음 경우의 수를 위해 만들어 놓은 테스트케이스를 더해주는 것
    
    return -1
