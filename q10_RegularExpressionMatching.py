# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s or not p:
            return False
        pre = ""
        flag = ""
        i = 0
        j = 0
        while s[i] != p[j] and (p[j] != "." or p[j] != "*"):
            if p[j] == ".":
                break
            j += 1
            if j >= len(p):
                return False
        print i, j
        while i < len(s):
            if j >= len(p):
                return False
            if s[i] == p[j]:
                pre = s[i]
                i += 1
                j += 1
            elif pre == s[i] and flag == "*":
                i += 1
                j += 1
            else:
                if p[j] == r'.':
                    pre = s[i]
                    i += 1
                    j += 1
                elif p[j] == r"*":
                    if not pre:
                        return False
                    else:
                        pre = s[i]
                        flag = r"*"
                        i += 1
                        j += 1
                else:
                    if s[i] == pre and flag == "*":
                        i += 1
                    else:
                        return False
        print i, j
        # while j < len(p):
        #     if p[j] != "*":
        #         return False
        #     j += 1
        return True

st = Solution()
# print st.isMatch("aa", "a")
# print st.isMatch("aa", "aa")
# print st.isMatch("aaa", "aa")
# print st.isMatch("aa", "a*")
# print st.isMatch("aa", ".*")
# print st.isMatch("ab", ".*")
# print st.isMatch("aab", "c*a*b")
# print st.isMatch("abcd", "d*")
# print st.isMatch("", ".*")
print st.isMatch("ab", ".*c")
print st.isMatch("aab", "c*a*b")
