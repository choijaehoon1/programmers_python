def solution(money):
    # 마지막 집과 첫번째집도 연결되어 있으면 안됨(원형구조 이므로)    
    answer = 0
    # 첫번째 집을 훔치는 경우
    dp_01 = [0] * len(money)
    dp_01[0] = money[0]
    dp_01[1] = max(money[0],money[1])
    for i in range(2,len(money)-1):
        dp_01[i] = max(dp_01[i-1], money[i] + dp_01[i-2])
    
    # 마지막 집을 훔치는 경우
    dp_02 = [0] * len(money)
    dp_02[0] = 0
    dp_02[1] = money[1]
    for i in range(2,len(money)):
        dp_02[i] = max(dp_02[i-1], money[i] + dp_02[i-2])
    
    answer = max(max(dp_01), max(dp_02))
    return answer
