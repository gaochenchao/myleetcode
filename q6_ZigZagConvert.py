# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return s
        if numRows == 1:
            return s
        res = []
        indexs = []
        seq = numRows + 1
        for i, v in enumerate(s):
            if i % seq == 0:
                res.append(v)
                indexs.append(i)
        for i, v in enumerate(s):
            if i % 2 != 0:
                res.append(v)
                indexs.append(i)
        for i, v in enumerate(s):
            if i not in indexs:
                res.append(v)

        return "".join(res)

st = Solution()
print st.convert("PAYPALISHIRING", 3)