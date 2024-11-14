def can_distribute(k, n, quantities):
    if k == 0:
        return False
    
    x = 0
    for q in quantities:
        x += ceil(q/k)
        print(x)

    return x <= n    

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if n == len(quantities):
            return max(quantities)
            
        left, right = 0, max(quantities)

        while left < right:
            mid = (left+right)//2

            if can_distribute(mid, n, quantities):
                right = mid
            else:
                left = mid + 1
        
        return left