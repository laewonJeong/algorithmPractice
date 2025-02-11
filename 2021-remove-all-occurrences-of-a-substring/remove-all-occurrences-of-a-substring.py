class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(s)
        m = len(part)
        
        for i in range(n):
            stack.append(s[i])
            if len(stack) >= m and ''.join(stack[-m:]) == part:
                for _ in range(m):
                    stack.pop()

        return ''.join(stack)