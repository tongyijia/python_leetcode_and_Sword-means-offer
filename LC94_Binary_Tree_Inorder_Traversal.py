# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root: return []

        def helper(root):
            if not root: return
            if not root.right and not root.left:
                res.append(root.val)
                return

            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root.left)
        res.append(root.val)
        helper(root.right)

        return res
