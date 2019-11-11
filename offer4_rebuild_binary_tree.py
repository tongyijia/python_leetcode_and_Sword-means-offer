# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre == [] or tin == []:
            return None

        parent = pre[0]
        index = tin.index(parent)
        l_tin = tin[:index]
        r_tin = tin[index+1:]
        l_pre = pre[1:1 + len(l_tin)]
        r_pre = pre[1 + len(l_tin):]
        root = TreeNode(parent)
        root.left = self.reConstructBinaryTree(l_pre, l_tin)
        root.right = self.reConstructBinaryTree(r_pre, r_tin)

        return root
