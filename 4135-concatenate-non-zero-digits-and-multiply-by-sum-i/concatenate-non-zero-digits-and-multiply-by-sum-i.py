class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
            
        x = ''
        sum = 0

        for num in str(n):
            if num != '0':
                sum += int(num)
                x += num
        
        return int(x) * sum