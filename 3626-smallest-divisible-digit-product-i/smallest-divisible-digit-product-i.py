class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def pd_digit(n):
            digit = 1
            
            while n > 0:
                digit *= (n % 10)
                n //= 10

            return digit
        
        while n < 101:
            product_digit = pd_digit(n)
            if product_digit % t == 0:
                return n
            
            n += 1