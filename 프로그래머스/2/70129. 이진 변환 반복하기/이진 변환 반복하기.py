def solution(s):
    a, b = 0, 0
    
    while s != '1':
        b += s.count('0')
        s = bin(s.count('1'))[2:]
        a += 1
    
    return [a, b]