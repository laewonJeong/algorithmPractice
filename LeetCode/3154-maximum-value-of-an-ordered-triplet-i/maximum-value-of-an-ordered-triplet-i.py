class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = 0
        for triplet in tuple(combinations(nums, 3)):
            answer = max(answer, (triplet[0] - triplet[1]) * triplet[2])
        
        return answer