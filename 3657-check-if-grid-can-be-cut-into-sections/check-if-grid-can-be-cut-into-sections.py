class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        n = len(rectangles)
        
        rectangles.sort()
        result = 0
        max_end = rectangles[0][2]
        for i in range(1, n):
            current_start = rectangles[i][0]
            current_end  = rectangles[i][2]

            if max_end <= current_start:
                result += 1
            if max_end < current_end:
                max_end = current_end

        if result + 1 >= 3:
            return True

        rectangles.sort(key = lambda x:x[1])
        result = 0
        max_end = rectangles[0][-1]
        for i in range(1, n):
            current_start = rectangles[i][1]
            current_end  = rectangles[i][-1]

            if max_end <= current_start:
                result += 1
            if max_end < current_end:
                max_end = current_end

        if result + 1 >= 3:
            return True

        return False