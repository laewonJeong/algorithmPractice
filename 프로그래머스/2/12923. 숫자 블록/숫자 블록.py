def max_divisor(n):
    if n == 1:
        return 0
    
    max_num = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if n // i <= 10000000:
                return n // i
            else:
                max_num = i
                
    if max_num != 0:
        return max_num
    return 1

def solution(begin, end):
    answer = []
    
    print(max_divisor(9))
    for i in range(begin, end+1):
        answer.append(max_divisor(i))
            
    return answer