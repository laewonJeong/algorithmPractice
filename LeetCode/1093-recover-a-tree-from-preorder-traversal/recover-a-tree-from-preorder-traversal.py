# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = []
        n = len(traversal)

        i = 0
        dash = 0
        digit = 0
        while i != n:
            if traversal[i].isdigit():
                if dash:
                    nodes.append(dash)
                    dash = 0
                digit= digit*10 + int(traversal[i])
            else:
                if digit:
                    nodes.append(digit)
                    digit=0
                dash += 1
            i+=1

        nodes.append(digit) # nodes = [1, '-', 401, '--', 349, '---', 90, '--', 88]
        n = len(nodes)
        root = TreeNode(nodes[0])
        
        def dfs(root, idx, depth):
            for lr in range(2):
                if idx + 2 < n and depth+1 == nodes[idx+1]:
                    if lr == 0:
                        root.left = TreeNode(nodes[idx+2])
                        idx = dfs(root.left, idx+2, depth+1)
                    else:
                        root.right = TreeNode(nodes[idx+2])
                        idx = dfs(root.right, idx+2, depth+1)
                else:
                    return idx
            return idx
        
        dfs(root, 0, 0)
        return root