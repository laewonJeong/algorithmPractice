class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter_s = Counter(s)
        n = len(s)
        right = 0
        check = []
        idx = -1
        answer = []
        for i in range(n):
            left = s[i]
            if not check or left not in check[idx]:
                if idx != -1:
                    answer.append(len(check[idx]))
                idx+=1
                check.append([])
            while counter_s[left] != 0 and right < n:
                counter_s[s[right]] -= 1
                check[idx].append(s[right])
                right += 1
        answer.append(len(check[-1]))
        return answer
        