# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root == None: return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, root1:TreeNode, root2:TreeNode) -> bool:

        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False

        if root1.val != root2.val: return False


        if not self.isMirror(root1.left, root2.right) or not self.isMirror(root1.right, root2.left):
            return False

        return True
