class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        answer = []
        
        if k == 0:
            return [0 for _ in range(n)]

        for i in range(n):
            idx = i
            temp = 0

            for _ in range(abs(k)):
                if k > 0:
                    idx += 1
                    if idx >= n:
                        idx -= n
                else:
                    idx -= 1
                    if idx < 0:
                        idx += n

                temp += code[idx]
            answer.append(temp)
            
        return answer
