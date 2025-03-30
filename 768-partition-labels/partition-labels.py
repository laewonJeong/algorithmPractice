class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter_s = Counter(s)
        n = len(s)
        right = 0
        check = []
        idx = -1
        
        for i in range(n):
            left = s[i]
            if not check or left not in check[idx]:
                idx+=1
                check.append([])
            while counter_s[left] != 0 and right < n:
                counter_s[s[right]] -= 1
                check[idx].append(s[right])
                right += 1
        
        answer = [0] * len(check)

        for i in range(len(check)):
            answer[i] = len(check[i])
        
        return answer
        