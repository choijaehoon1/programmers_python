def solution(clothes):
    close = {}
    for i in clothes:
        if i[1] in close:
            close[i[1]].append(i[0])
        else:
            close[i[1]] = [i[0]]
    
    cnt = 1
    for i in close.keys():
        cnt *= (len(close[i]) + 1)
    
    return cnt - 1
