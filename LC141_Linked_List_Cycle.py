# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if head == None: return False
        if head.next == None: return False

        slow = head
        fast = head.next

        while slow != None and fast != None:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if fast.next == None:
                    return False
                else:
                    fast = fast.next.next

        return False
