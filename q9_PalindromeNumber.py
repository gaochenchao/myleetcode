# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n = 0
        tmp = x
        while tmp > 0:
            tmp /= 10
            n += 1
        i = 1
        loop = n/2
        while i <= loop:
            if (x / (10 ** (n-1))) % 10 != x % 10:
                return False
            n -= 2
            x /= 10
            i += 1
        return True


st = Solution()
print st.isPalindrome(112321)
