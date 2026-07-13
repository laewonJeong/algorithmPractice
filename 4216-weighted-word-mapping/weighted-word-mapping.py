class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        answer = ''
        
        for word in words:
            weight_sum = 0
            
            for alpha in word:
                weight_sum += weights[ord(alpha) - 97]

            answer += chr(122 - weight_sum % 26)
        
        return answer