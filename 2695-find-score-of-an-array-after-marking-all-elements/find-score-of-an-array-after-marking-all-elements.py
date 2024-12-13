class Solution(object):
    def findScore(self, nums):
        n = len(nums)
        check = [False for i in range(n)]
        nums_with_indexes = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums_with_indexes)

        answer = 0
        check_cnt = 0
        while check_cnt != n:
            min_num, idx = heapq.heappop(nums_with_indexes)
            if not check[idx]:
                answer += min_num
                check[idx] = True
                check_cnt+=1
                if idx-1 >= 0 and not check[idx-1]:
                    check[idx-1] = True
                    check_cnt+=1
                if idx+1 < n and not check[idx+1]:
                    check[idx+1] = True
                    check_cnt+=1

        return answer
            


        