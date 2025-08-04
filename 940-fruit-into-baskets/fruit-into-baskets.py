class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        dic = defaultdict(int)
        left = 0
        right = 0
        answer = 0

        for left in range(n):
            while right < n and len(dic) <= 2:
                dic[fruits[right]] += 1
                right+=1
                if len(dic) <= 2:
                    answer = max(answer, right-left)
            
            dic[fruits[left]] -= 1
            if dic[fruits[left]] == 0:
                del dic[fruits[left]]
        
        return answer

        

        return 0