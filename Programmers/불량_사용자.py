case = [] 
cases = []

def recursion(start, end, available_based_len_bid, check):
    global case
    global cases 
    
    if start == end:
        cases.append(case[:])
        return case
    
    for i in range(start, len(available_based_len_bid)):
        for j in range(len(available_based_len_bid[i])):
            
            if check[available_based_len_bid[i][j]] != True:
                
                case.append(available_based_len_bid[i][j])
                check[available_based_len_bid[i][j]] = True
                
                case = recursion(start+1, end, available_based_len_bid, check)
                
                check[available_based_len_bid[i][j]] = False
                if len(case) != 0: case.pop()
                
        return case
        
def solution(user_id, banned_id):
    global cases
    
    available_based_len_bid = [[] for _ in range(len(banned_id))]
    check_dic = {}
    answer = []
    
    for idx, bi in enumerate(banned_id): 
        not_star = len(bi) - bi.count('*')
        for ui in user_id:
            cnt = 0
            if len(ui) == len(bi):    
                for u, b in zip(ui, bi):
                    if u == b: cnt+=1
                if cnt == not_star:
                    available_based_len_bid[idx].append(ui)
                    check_dic[ui] = False
                    
    recursion(0, len(banned_id), available_based_len_bid, check_dic)
    
    for c in cases:
        sc = sorted(c)
        if len(set(c)) == len(banned_id) and sc not in answer:
            answer.append(sc)

    return len(answer)
