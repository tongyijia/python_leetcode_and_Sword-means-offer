# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if not head or not head.next:  return None

        p = head
        fast = head
        for i in range(n):
            fast = fast.next
        
        #若删除的结点为第一个
        if not fast: return p.next

        while fast.next:
            fast = fast.next
            p = p.next

        if p.next.next:
            p.next.val = p.next.next.val
            p.next.next = p.next.next.next
        else:
            p.next = None


        return head
