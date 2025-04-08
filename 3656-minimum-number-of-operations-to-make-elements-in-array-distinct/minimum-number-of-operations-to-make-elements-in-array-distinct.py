class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = deque(nums)
        answer = 0
        while nums:
            counter_nums = Counter(nums)
            if all(value == 1 for value in counter_nums.values()):
                return answer

            for _ in range(3):
                if nums:
                    nums.popleft()
            
            answer += 1
        
        return answer