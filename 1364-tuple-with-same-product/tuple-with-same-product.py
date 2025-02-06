class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mul_value = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                mul_value[nums[i]*nums[j]]+=1
        
        answer = 0
        for v in mul_value.values():
            if v >= 2:
                for i in range(v):
                    answer += 8 * i
        return answer

