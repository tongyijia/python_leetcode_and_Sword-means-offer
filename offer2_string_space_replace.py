# -*- coding:utf-8 -*-
import re
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return re.sub(" ","%20",s)
