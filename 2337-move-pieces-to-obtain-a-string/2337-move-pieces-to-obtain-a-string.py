class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.count('_') != target.count('_'):
            return False
            
        n = len(start)
        j = 0

        for i in range(n):
            if target[i] == '_':
                continue
            while start[j] == '_':
                j+=1

            if start[j] != target[i]:
                return False
            elif start[j] == 'R' and target[i] == 'R' and j > i:
                return False
            elif start[j] == 'L' and target[i] == 'L' and j < i:
                return False
            else:
                j+=1

        return True