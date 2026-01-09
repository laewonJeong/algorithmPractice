def sum_of_digits(num):
    sum_num = 0
    while num != 0:
        sum_num += num % 10
        num //= 10
    
    return sum_num

class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_dic = defaultdict(int)

        for i in range(1, n+1):
            num = sum_of_digits(i)
            sum_dic[num] += 1
        
        max_cnt = max(sum_dic.values())
        
        answer = 0
        for key in sum_dic:
            if sum_dic[key] == max_cnt:
                answer += 1
        
        return answer