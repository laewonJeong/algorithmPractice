class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        n = len(rectangles)
        
        def can_cut(rectangles, dir):
            rectangles.sort(key = lambda x:x[dir])
            result = 0
            max_end = rectangles[0][dir+2]

            for i in range(1, n):
                start = rectangles[i][dir]
                end = rectangles[i][dir+2]

                if max_end <= start:
                    result += 1
                    if result == 2:
                        return True
                max_end = max(max_end, end)

            return result > 1

        return can_cut(rectangles, 0) or can_cut(rectangles, 1)