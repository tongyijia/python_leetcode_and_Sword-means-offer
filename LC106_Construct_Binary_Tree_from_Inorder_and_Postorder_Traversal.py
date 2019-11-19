# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None

        value = postorder.pop()
        p = TreeNode(value)
        i = inorder.index(value)

        p.left = self.buildTree(inorder[:i], postorder[:i])
        p.right = self.buildTree(inorder[i+1:], postorder[i:])
        return p
