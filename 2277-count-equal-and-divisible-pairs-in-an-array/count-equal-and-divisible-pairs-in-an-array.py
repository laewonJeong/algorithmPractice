class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        n = len(nums)
        answer = 0

        for i in range(n):
            dic[nums[i]].append(i)
        
        for v in dic.values():
            v_len = len(v)

            for i in range(v_len):
                for j in range(i+1, v_len):
                    if v[i] * v[j] % k == 0:
                        answer += 1
        
        return answer