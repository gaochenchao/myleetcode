# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        res = ""
        if str[0] == "+":
            str = str[1:]
        elif str[0] == "-":
            str = str[1:]
            res = "-"

        for i in str:
            if not i.isdigit():
                break
            res += i

        if res == "-" or not res:
            return 0
        res = int(res)
        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648
        return res

st = Solution()
print st.myAtoi("+-2")
