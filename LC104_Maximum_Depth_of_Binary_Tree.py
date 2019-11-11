# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root == None: return 0
        if not root.left and not root.right: return 1

        left_max = right_max = 0

        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)

        if left_max > right_max:
            return left_max + 1
        else:
            return right_max + 1
