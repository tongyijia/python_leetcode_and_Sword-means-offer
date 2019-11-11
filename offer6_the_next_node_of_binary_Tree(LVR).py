# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#思路：中序遍历的顺序为LVR
#则有以下三种情况：
#a. 如果该结点存在右子结点，那么该结点的下一个结点是右子结点树上最左子结点
#b. 如果该结点不存在右子结点，且它是它父结点的左子结点，那么该结点的下一个结点是它的父结点
#c. 如果该结点既不存在右子结点，且也不是它父结点的左子结点，则需要一路向祖先结点搜索，直到找到一个结点，该结点是其父亲结点的左子结点。如果这样的结点存在，那么该结点的父亲结点就是我们要找的下一个结点。
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return False

        if pNode.right:
            tmp = pNode.right
            while tmp.left:
                tmp = tmp.left
            return tmp

        p = pNode.next
        while p and p.right == pNode:
            pNode = p
            p = p.next

        return p
