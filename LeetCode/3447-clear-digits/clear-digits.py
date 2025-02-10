class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        n = len(s)

        for i in range(n):
            if not s[i].isdigit():
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
        
        return ''.join(stack)