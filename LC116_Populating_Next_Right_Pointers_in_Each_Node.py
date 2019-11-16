"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        head = root
        def helper(root):
            if not root or not root.left: return
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            helper(root.left)
            helper(root.right)
        helper(root)
        return head
