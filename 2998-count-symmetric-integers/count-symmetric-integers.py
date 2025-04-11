class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0
        for i in range(low, high+1):
            num = str(i)
            len_num = len(num)

            if len_num % 2 != 0:
                continue
            
            if sum(map(int, num[:len_num // 2])) == sum(map(int, num[len_num // 2:])):
                answer += 1 

        return answer