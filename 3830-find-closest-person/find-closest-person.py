class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_time = abs(x-z)
        y_time = abs(y-z)

        if x_time < y_time:
            return 1
        elif x_time > y_time:
            return 2
        else:
            return 0