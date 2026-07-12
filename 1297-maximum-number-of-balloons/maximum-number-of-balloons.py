class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        alpha_cnt = defaultdict(int)

        for alpha in text:
            alpha_cnt[alpha] += 1
        
        answer = 0
        while True:
            for alpha in 'balloon':
                alpha_cnt[alpha] -= 1
                if alpha_cnt[alpha] < 0:
                    return answer
            
            answer += 1
        return -1