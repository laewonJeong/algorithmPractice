class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = ''
        check = -1

        for i in range(1,len(num)-1):
            if num[i-1] == num[i] == num[i+1]:
                digit = int(num[i] * 3)
                if check < digit:
                    check = digit
                    answer = num[i] * 3
        
        return answer
