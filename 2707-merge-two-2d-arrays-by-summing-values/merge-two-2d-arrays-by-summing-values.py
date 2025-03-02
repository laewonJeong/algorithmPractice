class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        start = 0
        end = 0
        answer = []
        while start < n and end < m:
            id1, val1 = nums1[start]
            id2, val2 = nums2[end]

            if id1 == id2:
                answer.append([id1, val1 + val2])
                start += 1
                end += 1
            elif id1 < id2:
                answer.append([id1, val1])
                start += 1
            else:
                answer.append([id2, val2])
                end += 1
        
        while start < n:
            answer.append(nums1[start])
            start += 1
        while end < m:
            answer.append(nums2[end])
            end += 1

        return answer