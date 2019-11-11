# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True

        # find the mid node
        fast = head.next.next
        slow = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the pre part

        pre = None
        nex = None
        while head != slow:
            nex = head.next
            head.next = pre
            pre = head
            head = nex

        # if odd delete th later-part's first one
        if fast:
            slow = slow.next

        # check reverse
        while pre:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next

        return True
