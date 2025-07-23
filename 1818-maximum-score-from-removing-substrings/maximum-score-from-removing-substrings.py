def gain(ch1, ch2, s, x):
    before = []
    n = len(s)
    answer = 0

    for i in range(n):
        ch = s[i]

        if before and before[-1] == ch1 and ch == ch2:
            before.pop()
            answer += x
        else:
            before.append(ch)
    
    return answer, before

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        answer = 0

        if y > x:
            plus, s = gain('b', 'a', s, y)
            answer += plus
            plus, _ = gain('a', 'b', s, x)
            answer += plus
        else:
            plus, s = gain('a', 'b', s, x)
            answer += plus
            plus, _ = gain('b', 'a', s, y)
            answer += plus

        return answer