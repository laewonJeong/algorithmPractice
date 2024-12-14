class Solution:
    def getLucky(self, s: str, k: int) -> int:
        answer = 0

        for alpha in s:
            answer += (ord(alpha)-96)//10 + (ord(alpha)-96)%10

        k-=1
        while k!=0:
            temp = list((str(answer)))
            answer = 0
            for num in temp:
                answer += int(num)
            k-=1
        
        return answer