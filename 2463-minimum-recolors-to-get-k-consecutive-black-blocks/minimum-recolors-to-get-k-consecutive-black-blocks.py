class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        l = 0
        answer = n+1
        w_cnt = 0

        for r in range(n):
            if blocks[r] == 'W':
                w_cnt += 1
            
            if r - l + 1 == k:
                answer = min(answer, w_cnt)

                if blocks[l] == 'W':
                    w_cnt -= 1

                l+=1        
        
        return answer