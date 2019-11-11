#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        res = head = ListNode(0)
        carry = 0

        while l1 or l2:
            if l1 and l2:
                tmp = l1.val + l2.val + head.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                tmp = l1.val + head.val
                l1 = l1.next
            else:
                tmp = l2.val + head.val
                l2 = l2.next

            carry = tmp // 10
            head.val = tmp % 10
            head.next = ListNode(carry)
            pre = head
            head = head.next
        if carry == 0:
            pre.next = None

        return res
