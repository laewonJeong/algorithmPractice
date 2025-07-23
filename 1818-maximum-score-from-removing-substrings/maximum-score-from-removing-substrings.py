answer = 0

def gain(ch1, ch2, s, x):
    global answer
    before = []
    n = len(s)

    for i in range(n):
        ch = s[i]

        if before and before[-1] == ch1 and ch == ch2:
            before.pop()
            answer += x
        else:
            before.append(ch)
    
    return before

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        global answer
        answer = 0
        
        if y > x:
            s = gain('b', 'a', s, y)
            _ = gain('a', 'b', s, x)
        else:
            s = gain('a', 'b', s, x)
            _ = gain('b', 'a', s, y)
            
        return answer