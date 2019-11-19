# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        p = root
        s = 0
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            s += 1
            if s == k:
                return p.val
            p = p.right
