def solution(genres, plays):
    answer = []
    types = {} # 전체 종류
    genres_dict = {} # 장르별 재생
    for i in range(len(genres)):
        if genres[i] in types:
            genres_dict[genres[i]].append((plays[i],i)) # 재생수가 많은게 우선이므로 앞에 와야함
            types[genres[i]] += plays[i] 
        else:
            genres_dict[genres[i]] = [(plays[i],i)]
            types[genres[i]] = plays[i]
    
    types = sorted(types.items(), key = lambda a:a[1], reverse = True) # 재생수로 정렬해줘야함(비내림차순)
    # print(types)
    for i in types:
        key = i[0]
        play_list = genres_dict[key]
        play_list = sorted(play_list,key = lambda a:(-a[0],a[1])) # 재생횟수 같으면 숫자 낮게, 재생횟수가 많은 순

        for j in range(len(play_list)):
            if j == 2:
                break
            answer.append(play_list[j][1])    
            
    return answer
