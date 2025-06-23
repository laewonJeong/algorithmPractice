class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []

        temp = ''
        temp_len = 0
        for ch in s:
            temp += ch
            temp_len += 1
            if temp_len == k:
                answer.append(temp)
                temp = ''
                temp_len = 0
        
        if temp != '':
            temp += fill * (k - len(temp))
            answer.append(temp)
        
        return answer