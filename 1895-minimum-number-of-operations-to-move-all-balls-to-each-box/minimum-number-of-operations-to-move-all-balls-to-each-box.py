class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0 for _ in range(n)]

        for i in range(n):
            if boxes[i] == '1':
                for j in range(n):
                    if i == j:
                        continue
                    else:
                        answer[j] += abs(i-j)
        
        return answer