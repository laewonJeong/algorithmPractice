class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter_s = Counter(s)
        alpha = defaultdict(int)
        n = len(s)
        right = 0

        check = [[s[0]]]
        idx = 0
        for i in range(n):
            left = s[i]
            if left not in check[idx]:
                idx+=1
                check.append([])
            while counter_s[left] != 0 and right < n:
                counter_s[s[right]] -= 1
                check[idx].append(s[right])
                right += 1
        
        answer = [0] * len(check)

        for i in range(len(check)):
            if i == 0:
                answer[i] = len(check[i])-1
            else:
                answer[i] = len(check[i])
        
        return answer
        