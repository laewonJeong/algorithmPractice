class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        idx = defaultdict(int)
        for i, ele in enumerate(sorted(list(set(arr)))):
            idx[ele] = i + 1
        
        for i in range(len(arr)):
            arr[i] = idx[arr[i]]

        return arr