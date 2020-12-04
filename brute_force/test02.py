from itertools import permutations
import math
def sosu(n):
    sosu_list = [True] * (n + 1)
    for i in range(2,int(math.sqrt(n)) +1):
        j = 2
        if sosu_list[i] == True:
            while i*j <= n:
                sosu_list[i*j] = False
                j += 1
            
    return [i for i in range(2,n+1) if sosu_list[i] == True]

def solution(numbers):
    answer = 0
    num_list = list(numbers) # 리스트 만들기, 한자리 수는 일단 넣어두는 것
    
    for i in range(2, len(num_list)+1): # 2자리 수부터 permutations 수행(순서가 있으므로)
        pm = list(permutations(numbers,i))
        for j in pm:
            if len(j) <= len(numbers):
                num_list.append(''.join(j))
    
    num_list = list(set([int(i) for i in num_list])) # 중복 제거
    
    # 0과 1은 소수가 아님
    if num_list.count(0):
        num_list.remove(0)
    if num_list.count(1):
        num_list.remove(1)
        
    max_num = max(num_list) 
    sosu_list = sosu(max_num) # 가장 큰 값으로 소수 리스트 만들기
    for i in num_list:
        if i in sosu_list:
            # print(i)
            answer += 1
    
    return answer
