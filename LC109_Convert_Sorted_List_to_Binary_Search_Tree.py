# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if not head: return None
        if not head.next:
            p = TreeNode(head.val)
            return p

        slow = head
        fast = head
        pre = None

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        if pre:
            pre.next = None


        p = TreeNode(slow.val)
        if slow == head: return p
        p.left = self.sortedListToBST(head)
        p.right = self.sortedListToBST(mid)
        return p
