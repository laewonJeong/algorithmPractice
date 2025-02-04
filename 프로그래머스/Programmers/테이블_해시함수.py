def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x:x[0], reverse = True)
    data.sort(key = lambda x:x[col-1])
    
    for i in range(len(data)):
        temp = 0
        if row_begin <= i + 1 <= row_end:
            for d in data[i]:
                temp += d%(i+1)
            answer = answer ^ temp
            
    return answer
