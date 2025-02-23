# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}

        for parent, child, is_left in descriptions:
            nodes[child] = TreeNode(child)

        for parent, child, is_left in descriptions:
            if parent not in nodes:
                root = TreeNode(parent)
                nodes[parent] = root
                break
        
        for parent, child, is_left in descriptions:
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        return root