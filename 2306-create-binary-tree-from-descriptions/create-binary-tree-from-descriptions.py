# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        find_root = set()
        all_nodes = set()
        graph = defaultdict(lambda: [None, None])

        for parent, child, is_left in descriptions:
            find_root.add(child)
            all_nodes.add(parent)
            all_nodes.add(child)
            graph[parent][is_left ^ 1] = child

        root_val = list(all_nodes - find_root)[0]
        root = TreeNode(root_val)
        q = deque([root])
        
        while q:
            node = q.popleft()
            children = graph[node.val]

            if children[0] != None:
                node.left = TreeNode(children[0])
                q.append(node.left)

            if children[1] != None:
                node.right = TreeNode(children[1])
                q.append(node.right)

        return root
