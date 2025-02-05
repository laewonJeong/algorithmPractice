import heapq
def solution(plans):
    answer = []
    
    q = []
    for sub, st, d in plans:
        st = st.split(':')
        st = int(st[0]) * 60 + int(st[1])
        d = int(d)
        
        heapq.heappush(q, [st, d, sub])
    
    now_time = 0
    before_subject = ''
    temp = []
    
    while q:
        st, d, sub = heapq.heappop(q)
        
        if now_time > st:
            temp.append([now_time - st, before_subject])
        elif now_time == st:
            answer.append(before_subject)
        else:
            answer.append(before_subject)
            while temp:
                left_time, subject = temp.pop()
                if now_time + left_time <= st:
                    now_time += left_time
                    answer.append(subject)
                else:
                    temp.append([left_time - (st - now_time), subject])
                    break
                
        now_time = st+d
        before_subject = sub
        if not q:
            answer.append(sub)
    
    while temp:
        answer.append(temp.pop()[1])
    answer.pop(0)
    return answer