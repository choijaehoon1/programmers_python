def solution(citations):
    answer = 0
    citations.sort()
    # print(citations)
    for i in range(len(citations)):
        h = citations[i]        # 정렬하였으므로    0 1 3 5 6
        k = len(citations) - i  # k는 인용논문의 수 5 4 3 2 1
        if h >= k:
            answer = k # 인용논문의 수를 저장, 정렬 후 수행하는 것이라 반복할수록 인용논문의 수는 작아짐
            break
        
    return answer
