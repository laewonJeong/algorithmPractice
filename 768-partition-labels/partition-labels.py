class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for i, alpha in enumerate(s):
            last_idx[alpha] = i
        
        answer = []
        end = 0
        len_partition = 0
        for i, alpha in enumerate(s):
            end = max(end, last_idx[alpha])
            len_partition += 1
            if i == end:
                answer.append(len_partition)
                len_partition = 0

        return answer