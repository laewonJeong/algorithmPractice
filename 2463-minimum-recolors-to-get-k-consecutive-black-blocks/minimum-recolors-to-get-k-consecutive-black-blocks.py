class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        answer = n+1
        for i in range(n-k+1):
            answer = min(answer, blocks[i:i+k].count('W'))
            if answer == 0:
                return 0
        
        return answer