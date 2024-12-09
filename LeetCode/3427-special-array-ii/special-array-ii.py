class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        false_list = []
        answer = []

        for i in range(n-1):
            if (nums[i] % 2 == 0 and nums[i+1] %2 == 0) or (nums[i] % 2 != 0 and nums[i+1] %2 != 0):
                false_list.append((i, i+1))
        print(false_list)
        false_cnt = len(false_list)

        for query in queries:
            left, right = 0, false_cnt-1
            false_check = True
            while left <= right:
                mid = (left+right)//2
                if query[0] <= false_list[mid][0] <= query[1] and query[0] <= false_list[mid][1] <= query[1]:
                    false_check = False
                    break
                elif false_list[mid][1] <= query[0]:
                    left = mid+1
                else:
                    right = mid-1
            
            answer.append(false_check)
        
        return answer