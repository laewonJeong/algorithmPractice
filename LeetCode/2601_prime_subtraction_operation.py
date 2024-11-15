def make_prime_num(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    if n > 0:
        prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i]:
            j=2
            while i * j <= n:
                prime[i*j] = False
                j+=1

    return prime

def check_strictly_sort(nums):
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            return False
    return True

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
            
        max_num = max(nums)
        prime = make_prime_num(max_num)
        for j in range(nums[0]-1, -1, -1):
            if prime[j]:
                nums[0] -= j
                break

        for i in range(1, len(nums)):
            if check_strictly_sort(nums):
                return True

            for j in range(nums[i]-1, -1, -1):
                if prime[j] and nums[i] - j > nums[i-1]:
                    nums[i] -= j
                    break

        return False