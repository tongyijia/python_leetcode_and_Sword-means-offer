# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        levels = []
        if not root: return levels

        def help(root: TreeNode, level: int) -> None:

            if len(levels) == level :
                levels.append([])

            levels[level].append(root.val)

            if root.left:
                help(root.left, level+1)
            if root.right:
                help(root.right, level+1)

        help(root,0)

        return levels
