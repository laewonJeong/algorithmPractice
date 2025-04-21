class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        answer = 0
        temp = [lower]

        for difference in differences:
            temp.append(temp[-1] + difference)

        min1 = lower - min(temp)
        min2 = upper - max(temp)
        answer = min2 - min1 + 1
        
        return answer if answer > 0 else 0