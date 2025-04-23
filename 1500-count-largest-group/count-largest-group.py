class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_dic = defaultdict(int)
        max_cnt = 0

        for i in range(1, n+1):
            num = sum(map(int, str(i)))
            sum_dic[num] += 1
            max_cnt = max(max_cnt, sum_dic[num])
        
        answer = 0
        for key in sum_dic:
            if sum_dic[key] == max_cnt:
                answer += 1
        
        return answer