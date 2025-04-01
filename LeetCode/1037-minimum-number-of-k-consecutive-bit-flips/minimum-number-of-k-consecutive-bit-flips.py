class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip = 0
        answer = 0
        queue = deque()

        for i in range(n):
            if queue and queue[0] == i:
                queue.popleft()
                flip ^= 1
            
            if flip == nums[i]:
                if i + k > n:
                    return -1
                queue.append(i + k)
                flip ^= 1 
                answer += 1
        
        return answer