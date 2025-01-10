class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        answer = []
        n = len(words1)
        count_words2 = Counter(words2[0])

        for i in range(1, len(words2)):
            count_words2 |= Counter(words2[i])

        for word1 in words1:
            c1 = Counter(word1)
            check = True
            for key in count_words2:
                if c1[key] < count_words2[key]:
                    check = False
                    break
            if check:
                answer.append(word1)
                           

        return answer
