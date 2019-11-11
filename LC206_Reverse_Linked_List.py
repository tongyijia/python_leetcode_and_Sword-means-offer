# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head: return None
        if not head.next: return head

        tmp = head.next
        p = self.reverseList(tmp)
        tmp.next = head
        head.next = None
        return p
