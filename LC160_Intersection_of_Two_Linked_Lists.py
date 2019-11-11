# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #双指针

        if headA == None or headB == None: return None

        pA = headA
        pB = headB

        while pA or pB:
            if pA == pB:
                return pA
            elif pA.next == None and pB.next == None:
                return None
            else:
                if pA.next:
                    pA = pA.next
                else:
                    pA = headB
                if pB.next:
                    pB = pB.next
                else:
                    pB = headA

        return None
