def solution(number, k):
    answer = ''
    num = list(number)
    stack = [num[0]]
    
    cnt = 0
    
    for i in range(1,len(num)):
        if cnt == k:
            stack = stack + num[i:]
            break
        
        stack.append(num[i])
        
        if stack[-1] > stack[-2]:
            while len(stack) != 1 and stack[-1] > stack[-2] and cnt < k:
                stack[-2], stack[-1] = stack[-1], stack[-2]
                stack.pop()
                cnt += 1
    # print(stack)
    answer = "".join(stack[:len(num)-k])
    
    
    return answer
