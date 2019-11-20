# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head or not head.next: return head

        p_odd = head
        p2 = p_even = head.next
        i = 1
        p = head.next.next
        while p:
            if i == 0:
                p_even.next = p
                p_even = p_even.next
                i = 1
            else:
                p_odd.next = p
                p_odd = p_odd.next
                i = 0
            p = p.next
        if p_even.next: p_even.next = None
        p_odd.next = p2
        return head

            
