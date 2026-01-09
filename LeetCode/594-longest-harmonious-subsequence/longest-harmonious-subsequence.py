class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        answer = 0
        for num in nums:
            if num + 1 in count:
                answer = max(answer, count[num] + count[num+1])
        
        return answer