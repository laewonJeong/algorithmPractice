class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        rle = '1'
        for i in range(1, n):
            first = rle[0]
            cnt = 1
            temp = ''
            for j in range(1, len(rle)):
                if rle[j] == first:
                    cnt += 1
                else:
                    temp += str(cnt) + first
                    first = rle[j]
                    cnt = 1
            temp += str(cnt) + first
            rle = temp
            
        return rle