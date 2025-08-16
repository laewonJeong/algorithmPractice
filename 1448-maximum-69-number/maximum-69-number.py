class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        check = True
        answer = ''
        
        for i in range(len(num)):
            if num[i] == '6' and check:
                answer += '9'
                check = False
            else:
                answer += num[i]

        return int(answer)