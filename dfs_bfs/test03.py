answer = 0

def dfs(begin, target, words, visit):
    global answer
    stack = [begin]
    while stack:
        current_node = stack.pop()
        if current_node == target:
            return answer
        
        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != current_node[j]]) == 1 and visit[i] == 0:
                visit[i] = 1
                stack.append(words[i])
        answer+=1                    

        
def solution(begin, target, words):
    global answer
    visit = [0 for _ in range(len(words))]
    if target not in words:
        return 0
    
    dfs(begin, target, words, visit)
    
    return answer
