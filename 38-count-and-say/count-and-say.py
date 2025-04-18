class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        rle = '1'
        rle_len = 1
        for i in range(1, n):
            first = rle[0]
            cnt = 1
            temp = ''
            l = 0
            for j in range(1, rle_len):
                if rle[j] == first:
                    cnt += 1
                else:
                    temp += str(cnt) + first
                    l += 2
                    first = rle[j]
                    cnt = 1
            temp += str(cnt) + first
            l+=2
            rle = temp
            rle_len = l
            
        return rle