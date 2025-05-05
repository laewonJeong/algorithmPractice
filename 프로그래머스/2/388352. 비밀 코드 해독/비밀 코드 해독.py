from itertools import combinations

def check(q, ans, comb):
    for i in range(len(q)):
        if len(comb & set(q[i])) != ans[i]:
            return False
    
    return True

def solution(n, q, ans):
    answer = 0
    num = [i for i in range(1,n+1)]
    
    for comb in tuple(combinations(num, 5)):
        if check(q, ans, set(comb)):
            answer += 1
        
    return answer