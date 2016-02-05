# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 0
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        m = x
        while m > 0:
            m /= 10
            n += 1
        r = 0
        while n > 0:
            r += (x % 10) * pow(10, n-1)
            if r > (2**31-1):
                return 0
            x /= 10
            n -= 1
        if flag:
            r = -r
        return r


st = Solution()
st.reverse(-123)