class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for i, alpha in enumerate(s):
            last_idx[alpha] = i
        
        answer = []
        start, end = 0, 0
        for i, alpha in enumerate(s):
            end = max(end, last_idx[alpha])
            if i == end:
                answer.append(end-start+1)
                start = i + 1

        return answer