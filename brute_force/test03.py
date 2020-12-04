def solution(brown, yellow):
    answer = [0,0]
    board = brown + yellow
    
    for i in range(3,board):
        if board % i == 0:
            column = i
            row = board // column
            if (row-2) * (column-2) == yellow and row>=column:
                answer[0] = row
                answer[1] = column
    return answer
