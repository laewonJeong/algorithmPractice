class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        temp_box = []

        for b in box:
            split_obstacle = []
            temp = deque()
            for c in b:
                if c == '*':
                    split_obstacle.append(temp)
                    temp = deque()
                    continue
                temp.append(c)
            split_obstacle.append(temp)

            for so in split_obstacle:
                empty_cnt = 0
                while '.' in so:
                    so.remove('.')
                    empty_cnt += 1
                for _ in range(empty_cnt):
                    so.appendleft('.')

            temp = ''
            for so in split_obstacle:
                temp += ''.join(so)
                temp += '*'
            
            temp_box.append(list(temp))
        
        n = len(box)
        m = len(box[0])
        rotate_box = [[] for _ in range(m)]

        for i in range(m):
            for j in range(n-1, -1, -1):
                rotate_box[i].append(temp_box[j][i])
        
        return rotate_box
