# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.vertex = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.vertex

    def bfs(self, root, x):
        q = deque([(root, x)])

        while q:
            root, x = q.popleft()
            self.vertex.add(x)
            if root.left:
                q.append((root.left, 2 * x + 1))
            if root.right:
                q.append((root.right, 2 * x + 2))
    
    def dfs(self, root, x):
        self.vertex.add(x)

        if root.left:
            self.dfs(root.left, 2 * x + 1)
        if root.right:
            self.dfs(root.right, 2 * x + 2)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)