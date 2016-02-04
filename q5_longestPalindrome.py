# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        maxl, maxr, length = 0, 0, 0
        n = len(s)
        for i in xrange(n):
            start = i
            end = i + 1
            while start >= 0 and end < n:
                if s[start] == s[end]:
                    if end - start + 1 > length:
                        maxl, maxr, length = start, end, end - start + 1
                    start -= 1
                    end += 1
                else:
                    break

            start = i - 1
            end = i + 1
            while start >= 0 and end < n:
                if s[start] == s[end]:
                    if end - start + 1 > length:
                        maxl, maxr, length = start, end, end - start + 1
                    start -= 1
                    end += 1
                else:
                    break
        return s[maxl:maxr+1]
st = Solution()
print st.longestPalindrome("aaaaa")