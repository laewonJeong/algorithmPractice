class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        range_list = []
        n = len(nums)

        for num in nums:
            range_list.append((max(0, num-k), num+k))
        
        range_list.sort(key=lambda x:(x[0],x[1]))

        answer = 0

        for i in range(n):
            start, end = range_list[i]
            left, right = i, n - 1 
            while left <= right:
                mid = (left + right) // 2
                if range_list[mid][0] <= range_list[i][1]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            print(right-i+1)
            answer = max(answer, right - i + 1)
        
        return answer