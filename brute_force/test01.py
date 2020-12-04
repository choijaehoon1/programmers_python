def solution(answers):
    answer = []
    supo_01 = [1,2,3,4,5]
    supo_02 = [2,1,2,3,2,4,2,5]
    supo_03 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt_list = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == supo_01[i%5]:
            cnt_list[0] += 1
        if answers[i] == supo_02[i%8]:
            cnt_list[1] += 1    
        if answers[i] == supo_03[i%10]:
            cnt_list[2] += 1    
    
    if max(cnt_list) == cnt_list[0] and max(cnt_list) == cnt_list[1] and max(cnt_list) == cnt_list[2]:
        return [1,2,3]
    elif max(cnt_list) == cnt_list[0] and max(cnt_list) == cnt_list[1]:
        return [1,2]
    elif max(cnt_list) == cnt_list[0] and max(cnt_list) == cnt_list[2]:
        return [1,3]
    elif max(cnt_list) == cnt_list[1] and max(cnt_list) == cnt_list[2]:
        return [2,3]
    elif max(cnt_list) == cnt_list[0]:
        return [1]
    elif max(cnt_list) == cnt_list[1]:
        return [2]
    elif max(cnt_list) == cnt_list[2]:
        return [3]
