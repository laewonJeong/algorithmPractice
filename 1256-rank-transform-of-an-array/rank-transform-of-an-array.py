class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        idx = defaultdict(int)
        for i, ele in enumerate(sorted(list(set(arr)))):
            idx[ele] = i + 1
        
        return [idx[arr[i]] for i in range(len(arr))]